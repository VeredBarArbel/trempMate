from flask import Blueprint, render_template, request, redirect, url_for, flash
from utilities import general

# SearchARide blueprint definition
SearchARide = Blueprint('SearchARide', __name__, static_folder='static', static_url_path='/SearchARide', template_folder='templates')


# Routes
@SearchARide.route('/SearchARide')
def index():
    return render_template('SearchARide.html')


@SearchARide.route('/showDetails', methods=['POST'])
def showDetails():
    # show relevant links
    startCity = request.form['rideFrom']
    endCity = request.form['rideTo']
    date = request.form['date']
    search = general.search_ride(startCity, endCity, date)
    if search == False:
        flash("Couldn't find relevant trips for you")
    showDetails = True
    return render_template('SearchARide.html', search=search, showDetails=showDetails)
