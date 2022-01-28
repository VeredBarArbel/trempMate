from flask import Blueprint, render_template, session, flash, request, redirect
from utilities import general
from datetime import datetime

# History blueprint definition
RideHistory = Blueprint('RideHistory', __name__, static_folder='static', static_url_path='/RideHistory',
                        template_folder='templates')


# Routes
@RideHistory.route('/RideHistory')
def index():
    # get rides where I'm the driver
    today = datetime.now().date()
    driver = general.driver_history(session['email'])
    tremp = general.tremp_history(session['email'])
    if not driver and not tremp:
        flash("No rides were found")
    return render_template('RideHistory.html', driver=driver, tremp=tremp, today=today)

@RideHistory.route('/removeReg', methods=['POST'])
def remove_registration():
    user = request.form['user']
    trip = request.form['trip']
    general.remove_reg(user, trip)
    return redirect('/RideHistory')
