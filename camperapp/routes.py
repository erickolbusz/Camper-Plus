"""Routes for Camper+ app."""

from camperapp import app
from flask import render_template
from flask import jsonify
from flask import request


# sample data, replace with db query
groups = [{"name": "Tigers", "color": "#4286f4", "groupid": 1},
          {"name": "Falcons", "color": "#af2313", "groupid": 2},
          {"name": "Bears", "color": "#191917", "groupid": 3},
          {"name": "Lions", "color": "#FB8CB5", "groupid": 4},
          {"name": "Jacks", "color": "#C9B09C", "groupid": 5}]


@app.route('/', methods=['GET'])
def index():
    """View displays the homepage"""
    return "<h1>Welcome To Camper+</h1>"


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    """View displays the schedule-making page"""
    return render_template("schedule.html", groups=groups)

@app.route('/campers', methods=['GET'])
def campers():
    """View displays the camper organization page"""
    return render_template("campers.html")

@app.route('/saveEvent', methods=['POST'])
def submit_handler():
    # a = request.get_json(force=True)
    event_data = request.json
    group_id = event_data['group']
    group = next(item for item in groups if item["groupid"] == int(group_id))
    color = group['color']

    return jsonify({'msg': 'success', 'color': color})
