"""Routes for Camper+ app."""

from camperapp import app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    """View displays the homepage"""
    return "<h1>Welcome To Camper+</h1>"

@app.route('/schedule', methods=['GET', 'POST', 'PUT', 'DELETE'])
def schedule():
    """View displays the schedule-making page"""
    #sample data, replace with db query
    groups = [{"name":"Cool Group", "color": "#4286f4", "groupid": 1},
              {"name":"Annoying Kids", "color": "#af2313", "groupid": 2}]
    return render_template("schedule.html",groups=groups)