from flask import Blueprint, render_template, redirect, url_for, request, flash
from utilities.classes.ContactDetails import Contact

# ContactUs blueprint definition
ContactUs = Blueprint('ContactUs', __name__, static_folder='static', static_url_path='/ContactUs', template_folder='templates')


# Routes
@ContactUs.route('/ContactUs')
def contact():
    return render_template('contactUs.html')


@ContactUs.route('/submitContactReq', methods=['POST'])
def submitContact():
    email = request.form['contactEmail']
    description = request.form['contactDescription']
    # add req to DB
    newContactReq = Contact(email, description)
    newContactReq.create_req()
    flash("Your request has been submitted, talk to you soon (:")
    return redirect(url_for('ContactUs.contact'))


