"""Routes for Camper+ app."""

from camperapp import app
from camperapp.models import db, CampEvent, CampGroup
from flask import render_template
from flask import jsonify
from flask import request


@app.route('/', methods=['GET'])
def index():
    """View displays the homepage"""
    return "<h1>Welcome To Camper+</h1>"

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    """View displays the schedule-making page"""
    groups = CampGroup.query.all()
    return render_template("schedule.html", groups=groups)

@app.route('/campers', methods=['GET'])
def campers():
    """View displays the camper organization page"""
    return render_template("campers.html")

@app.route('/login', methods=['GET'])
def login():
    """View displays the login page"""
    return render_template("login.html")

@app.route('/saveEvent', methods=['POST', 'PUT'])
def submit_handler():
    # a = request.get_json(force=True)

    if request.method == 'POST':
        event_data = request.json

        # save event to database
        event = CampEvent.convert_calevent_to_campevent(event_data)
        db.session.add(event)
        db.session.commit()

        # query database for group color and event id
        color = event.campgroup.color
        event_id = event.id

        return jsonify({'msg': 'success', 'color': color, 'id': event_id})

    elif request.method == 'PUT':
        print("Received a PUT request of event")
        return jsonify({'msg': 'success'})
