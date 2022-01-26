from flask import Blueprint, render_template, session, request, redirect
from utilities.db.db_manager import dbeWelcome
from utilities.classes.User import User
from utilities import general

# Welcome blueprint definition
Welcome = Blueprint('Welcome', __name__, static_folder='static', static_url_path='/Welcome', template_folder='templates')

# think about db
# Routes
@Welcome.route('/Login')
@Welcome.route('/')
def welcome():
    session.clear()
    return render_template('Welcome.html')


@Welcome.route('/signup', methods=['post'])
def signup():
    session.clear()
    password = request.form['signuppass']
    email = request.form['Gmail']
    user_fname = request.form['fname']
    user_lname = request.form['lname']
    return dbeWelcome.addUser(email=email, fname=user_fname, lname=user_lname, password=password)

@Welcome.route('/signIn', methods=['post'])
def signIn():
    password = request.form['password']
    email = request.form['email']
    user = general.get_user(email)
    if user != '': #user exist
        if user.check_password(password): #matching password
            user.user_session()
            return redirect('/home')
    return redirect('/Login') #user doesn't wxist or password doesn't match
