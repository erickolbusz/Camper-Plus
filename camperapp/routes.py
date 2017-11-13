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
    # sample data, replace with db query
    groups = [{"name": "Tigers", "color": "#4286f4", "groupid": 1},
              {"name": "Falcons", "color": "#af2313", "groupid": 2},
              {"name": "Bears", "color": "#191917", "groupid": 3},
              {"name": "Lions", "color": "#FB8CB5", "groupid": 4},
              {"name": "Jacks", "color": "#C9B09C", "groupid": 5}]
    return render_template("schedule.html", groups=groups)
