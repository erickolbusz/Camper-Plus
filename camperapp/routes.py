"""Routes for Camper+ app."""

from camperapp import app
from camperapp.models import db, CampEvent, CampGroup, CampEventSchema
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


@app.route('/saveEvent', methods=['POST', 'PUT', 'DELETE'])
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
        event_data = request.json

        event_id = int(event_data['id'])
        new_title = event_data['title']
        new_start = CampEvent.convert_ISO_datetime_to_py_datetime(event_data['start'])
        new_end = CampEvent.convert_ISO_datetime_to_py_datetime(event_data['end'])
        new_group_id = int(event_data['group_id'])

        CampEvent.query.filter_by(id=event_id).update({'title': new_title, 'start': new_start,
                                                       'end': new_end, 'group_id': new_group_id})
        db.session.commit()

        return jsonify({'msg': 'success'})

    elif request.method == 'DELETE':
        print('Received a Delete Request')
        event_data = request.json
        event_id = int(event_data['id'])
        print(event_id)

        return jsonify({'msg': 'success'})


@app.route('/getCampEvents', methods=['GET'])
def get_camp_events():
    start = request.args.get('start')  # get events on/after start
    end = request.args.get('end')    # get events before/on end
    print(start, end)

    event_schema = CampEventSchema(many=True)
    events = CampEvent.query.all()   # get all data for now

    for event in events:
        event.add_color_attr()

    result = event_schema.dump(events).data

    return jsonify(result)
