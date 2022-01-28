from flask import Blueprint, render_template, request, redirect, url_for, flash
from utilities import general

# SearchARide blueprint definition
SearchARide = Blueprint('SearchARide', __name__, static_folder='static', static_url_path='/SearchARide',
                        template_folder='templates')


# Routes
@SearchARide.route('/SearchARide')
def index():
    cities = general.city()
    return render_template('SearchARide.html', cities=cities)


@SearchARide.route('/showDetails', methods=['POST'])
def showDetails():
    # show relevant links
    cities = general.city()
    startCity = request.form['rideFrom']
    endCity = request.form['rideTo']
    date = request.form['date']
    search = general.search_ride(startCity, endCity, date)
    if search == "Couldn't find relevant trips for you":
        flash("Couldn't find relevant trips for you")
        search = False
    elif search == False: #inserted date already passed
        flash("You can't register for a past trip")
    showDetails = True
    return render_template('SearchARide.html', search=search, showDetails=showDetails, cities=cities)
