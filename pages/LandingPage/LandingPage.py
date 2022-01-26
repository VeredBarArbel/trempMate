from flask import Blueprint, render_template, redirect, url_for, session

# LandingPage blueprint definition
LandingPage = Blueprint('LandingPage', __name__, static_folder='static', static_url_path='/LandingPage', template_folder='templates')


# Routes
@LandingPage.route('/home')
def index():
    return render_template('LandingPage.html')


# @LandingPage.route('/LandingPage')
# @LandingPage.route('/home')
# def redirect_homepage():
#     return redirect(url_for('LandingPage.index'))
