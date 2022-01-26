from flask import Blueprint, render_template, session, request, redirect, url_for
from utilities.classes.Trip import Trip
from datetime import datetime
# AddARide blueprint definition
AddARide = Blueprint('AddARide', __name__, static_folder='static', static_url_path='/AddARide', template_folder='templates')


# Routes
@AddARide.route('/AddARide')
def index():
    return render_template('AddARide.html')

@AddARide.route('/submitARide' ,methods=['POST'])
def submitARide():
    driver = session['email'] #CREATE SESSION
    pickupCity = request.form['goesFrom']
    dropCity = request.form['dropAt']
    price = request.form['price']
    date = request.form['rideDate']
    time = request.form['rideHour']
    passengers = request.form['passengers']
    #insert ride to DB
    newTrip = Trip(driver, date, time, pickupCity, dropCity, passengers, price)
    newTrip.create_trip()
    #return the ride page in Join a ride
    return redirect('/AddARide')


