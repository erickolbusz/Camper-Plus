"""Models in Camper APP"""

api_key = "AIzaSyDfnLfxNeG45N_tBtUutrB9K6-GYCtD7_I"


from camperapp import app
from app import db
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

class CampEvent(db.Model):
    __tablename__='events'
    event_id = db.Column(db.Integer, primary_key = True)
    event_title = db.Column(db.String())
    event_start = db.Column(db.String())
    events_end = db.Column(db.String())
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)



    """Camp Event class representing an event on the calendar"""

    def __init__(self, event_title,event_start,events_end,group_id):
        self.event_title = event_title.title()
        self.event_start = event_start.title()
        self.event_end = event_end.title()
        self.eroup_id = group_id.title()

        """ it is not final """
    def __repr__(self):
        return '<CampEvent {}>'.format(self.title)

    def load_all_appointments_in_range(cls, start, end):
        """
        Returns all Events between start date and end date as a list
        param start: start date as a unix time string
        param end: end date as a unix time string
        return: a list of camp events
        """
        start_date = CampEvent.convert_from_unix_time_stamp(start)
        end_date = CampEvent.convert_from_unix_time_stamp(end)

        # TODO
        events = CampEvent.query.all()
        for event in events:
    post.user_name = User.query.filter_by(id=post.id).first()
return render_template('post.html', entries=posts)
        # Query database and retrieve all appointments between start and end
        # Store results in result
        query_result = None(start_date, end_date)

        calendar_events = []
        for item in query_result:
            event = CampEvent()
            event.id = item.ID
            event.title = item.Title
            event.start_date = item.start_date
            event.end_date = item.end_date
            event.color = item.color
            event.groups = item.group

            calendar_events.append(event)

        return calendar_events

    # TODO
    def get_camp_events(cls, start, end):
        """
        Returns all events between start date and end date as a json
        param start: start date as a unix time string
        param end: end date as a unix time string
        return: a json containing camp events between start and end date
        """
        event_data = CampEvent.load_all_appointments_in_range(start, end)

        #TODO parse event_data to JSON

        return None

    # TODO
    def update_camp_event(cls, id, new_event_start, new_event_end):
        """Update an existing event"""
        # EventStart comes ISO 8601 format, eg:  "2000-01-10T10:00:00Z"
        # - need to convert to DateTime

        # query database and retrieve the event matching the ID
        result = None

        if result is not None:
            # convert dates to database friendly date time
            # Update the database with the new start and end date
            pass

        return None

    # TODO
    def convert_from_unix_time_stamp(cls, date):
        """
        Converts a unix time stamp to database friendly timestamp
        """
        pass
>>>>>>> camper/master

class Group(db.Model):
    __tablename__='group'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String())
    color = db.Column(db.String())
    quantity = db.Column(db.Integer())
    camperevents = db.relationship('CampEvent', backref = 'group',lazy = 'dynamic')
    camper1_id = db.Column(db.Integer(), db.ForeignKey('camper.id', nullable=False)
    camper2_id = db.Column(db.Integer(), db.ForeignKey('camper.id', nullable=False)
    camper3_id = db.Column(db.Integer(), db.ForeignKey('camper.id', nullable=False)
    camper4_id = db.Column(db.Integer(), db.ForeignKey('camper.id', nullable=False)
    camper5_id = db.Column(db.Integer(), db.ForeignKey('camper.id', nullable=False)

    def __repr__(self):
        return '<Group {}>'.format(self.name)


class Parent(db.Model):
    __tablename__='parent'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    phone_number = db.Column(db.String())
    camper_id = db.Column(db.Integer, db.ForeignKey('camper.id'), nullable=False)
    campers = db.relationship('Camper',backref = 'parent',lazy = 'dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_active(self):
        return self.active is None or self.active

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Parent {}>'.format(self.name)


class Camper(db.Model):
    __tablename__='camper'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    age = db.Column(db.Integer())
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    groups = db.relationship('Groups',backref = 'camper',lazy = 'dynamic')
    parents = db.relationship('Parent',backref = 'camper',lazy = 'dynamic')
    def __repr__(self):
        return '<Camper {}>'.format(self.name)


class CampWorker(db.Model):
    __tablename__='camperworker'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    position = db.Column(db.String())
    def __repr__(self):
        return '<CampWorker {}>'.format(self.name)
