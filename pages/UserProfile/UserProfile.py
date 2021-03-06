from flask import Blueprint, render_template, session, request, redirect, flash
from utilities import general

# UserProfile blueprint definition
UserProfile = Blueprint('UserProfile', __name__, static_folder='static', static_url_path='/UserProfile', template_folder='templates')


# Routes
@UserProfile.route('/UserProfile')
def index():
    # show relevant data - user info from session UPDATE SESSION
    return render_template('UserProfile.html')


@UserProfile.route('/updateProfile', methods=['POST'])
def updateProfile():
    # show relevant data - user info
    fname = request.form['first_name']
    lname = request.form['last_name']
    about = request.form['about_me']
    password = request.form['password']
    phone = request.form['phone']
    carType = request.form['car_type']
    carColor = request.form['car_color']
    user = general.get_user(session['email'])
    if user.update_user(fname, lname, about, phone, password, carType, carColor):
        user.user_session()
        flash("You're all set up!")
    else:
        flash("Something went wrong, please try again")
    return redirect('/UserProfile')
