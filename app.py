from flask import Flask, session


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages

## Welcome
from pages.Welcome.Welcome import Welcome
app.register_blueprint(Welcome)

## Homepage
from pages.LandingPage.LandingPage import LandingPage
app.register_blueprint(LandingPage)

## About
from pages.aboutUs.aboutUs import aboutUs
app.register_blueprint(aboutUs)

## ContactUs
from pages.ContactUs.contactUs import ContactUs
app.register_blueprint(ContactUs)

## RideDetails
from pages.RideDetails.RideDetails import RideDetails
app.register_blueprint(RideDetails)

## AddARide
from pages.AddARide.AddARide import AddARide
app.register_blueprint(AddARide)

## SearchARide
from pages.SearchARide.SearchARide import SearchARide
app.register_blueprint(SearchARide)

## UserProfile
from pages.UserProfile.UserProfile import UserProfile
app.register_blueprint(UserProfile)
#
# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)

# ###### Components
# ## Main menu
# from components.main_menu.main_menu import main_menu
# app.register_blueprint(main_menu)

if __name__ == '_main_':
    app.run(debug=True)