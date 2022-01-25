from flask import Blueprint, render_template, session, request, redirect
from utilities.db.db_manager import dbeWelcome

# Welcome blueprint definition
Welcome = Blueprint('Welcome', __name__, static_folder='static', static_url_path='/Welcome', template_folder='templates')

# think about db
# Routes
@Welcome.route('/Login')
def welcome():
    return render_template('Welcome.html')


@Welcome.route('/signup', methods=['post'])
def signup():
    session.clear()
    password = request.form['signuppass']
    email = request.form['Gmail']
    user_fname = request.form['fname']
    user_lname = request.form['lname']
    return dbeWelcome.addUser(email=email, fname=user_fname, lname=user_lname, password=password)
