from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities import general

# RideDetails blueprint definition
RideDetails = Blueprint('RideDetails', __name__, static_folder='static', static_url_path='/RideDetails',
                        template_folder='templates')


# Routes
@RideDetails.route('/RideDetails', defaults={'tripID': -1})
@RideDetails.route('/RideDetails/<int:tripID>')
def index(tripID):
    if tripID != -1:  # got a trip id
        # show relevant data from DB
        tripRow = general.get_trip(tripID)
        if tripRow != False:  # found your trip
            trip_id = tripRow[0]
            tripDriver = tripRow[1]
            tripDate = tripRow[2]
            tripTime = tripRow[3]
            tripStartCity = tripRow[4]
            tripDestCity = tripRow[5]
            tripSeats = tripRow[6]
            tripPrice = tripRow[7]
            return render_template('RideDetails.html', trip_id=trip_id, tripDriver=tripDriver, tripDate=tripDate,
                                   tripTime=tripTime, tripStartCity=tripStartCity, tripDestCity=tripDestCity,
                                   tripSeats=tripSeats, tripPrice=tripPrice)
    # got no trip id/couldn't find id
    return redirect(url_for('SearchARide.index'))


@RideDetails.route('/SaveASpot', methods=['POST'])
def SaveASpot():
    tripID = request.form['trip_id']
    amount = request.form['amount']
    # add to DB if there are available spots left
    save = general.save_spot(tripID, session['email'], amount)
    if save == "not enough seats":
        flash("Oh no, we couldn't save a spot because there are not enough seats. " \
                          "Try again!")
    elif save == "already registered":
        flash("You are already register to this trip")
    else:
        flash("%s spots saved successfully!" %amount)
    #enough seats
    return redirect(f'/RideDetails/{tripID}')
