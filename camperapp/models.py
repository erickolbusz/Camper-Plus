"""Models in Camper APP"""
# from camperapp import app
from camperapp import db
# from werkzeug import generate_password_hash, check_password_hash


class CampEvent(db.Model):
    """Camp Event class representing an event on the calendar"""
    __tablename__ = 'event'
    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    start = db.Column(db.DateTime())
    end = db.Column(db.DateTime())

    def __repr__(self):
        return '<CampEvent {}>'.format(self.title)


db.create_all()
db.session.commit()

# class Group(db.Model):
#     __tablename__='group'
#     id = db.Column(db.Integer(), primary_key = True)
#     name = db.Column(db.String())
#     color = db.Column(db.String())
#     quantity = db.Column(db.Integer())
#     camperevents = db.relationship('CampEvent', backref = 'group',
#                         lazy = 'dynamic')
#     camper_id = db.Column(db.Integer(), db.ForeignKey('camper.id', nullable=False)
#     campers = db.relationship('Camper',backref = 'group',lazy = 'dynamic')
#
#     def __repr__(self):
#         return '<Group {}>'.format(self.name)
#
#
# class Parent(db.Model):
#     __tablename__='parent'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String())
#     email = db.Column(db.String())
#     password = db.Column(db.String())
#     phone_number = db.Column(db.String())
#     camper_id = db.Column(db.Integer, db.ForeignKey('camper.id'), nullable=False)
#     campers = db.relationship('Camper',backref = 'parent',lazy = 'dynamic')
#
#     def set_password(self, password):
#         self.password = generate_password_hash(password)
#
#     def check_password(self, value):
#         return check_password_hash(self.password, value)
#
#     def is_active(self):
#         return self.active is None or self.active
#
#     def get_id(self):
#         return self.id
#
#     def __repr__(self):
#         return '<Parent {}>'.format(self.name)
#
#
# class Camper(db.Model):
#     __tablename__='camper'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String())
#     email = db.Column(db.String())
#     password = db.Column(db.String())
#     age = db.Column(db.Integer())
#     parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
#     group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)
#     groups = db.relationship('Groups',backref = 'camper',lazy = 'dynamic')
#     parents = db.relationship('Parent',backref = 'camper',lazy = 'dynamic')
#
#     def get_id(self):
#         return self.id
#
#
#     def __repr__(self):
#         return '<Camper {}>'.format(self.name)
#
#
# class CampWorker(db.Model):
#     __tablename__='camperworker'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String())
#     email = db.Column(db.String())
#     password = db.Column(db.String())
#     position = db.Column(db.String())
#     def __repr__(self):
#         return '<CampWorker {}>'.format(self.name)
