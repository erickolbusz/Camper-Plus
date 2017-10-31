"""Routes for Camper+ app."""

from camperapp import app


@app.route('/', methods=['GET'])
def index():
    """View displays the homepage"""
    return "<h1>Welcome To Camper+</h1>"

@app.route('/schedule', methods=['GET','POST'])
def schedule():
    """View displays the schedule-making page"""
    return "<h1>placeholder</h1>"
