from flask import Blueprint, render_template

# SearchARide blueprint definition
SearchARide = Blueprint('SearchARide', __name__, static_folder='static', static_url_path='/SearchARide', template_folder='templates')


# Routes
@SearchARide.route('/SearchARide')
def index():
    return render_template('SearchARide.html')


@SearchARide.route('/showDetails', methods=['POST'])
def showDetails():
    # show relevant links
    return render_template('SearchARide.html')
