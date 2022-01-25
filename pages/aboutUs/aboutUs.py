from flask import Blueprint, render_template

# aboutUs blueprint definition
aboutUs = Blueprint('aboutUs', __name__, static_folder='static', static_url_path='/aboutUs', template_folder='templates')


# Routes
@aboutUs.route('/AboutUs')
def index():
    return render_template('AboutUs.html')
