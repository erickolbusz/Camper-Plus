"""Google Calendar API configuration"""

api_key = "AIzaSyDfnLfxNeG45N_tBtUutrB9K6-GYCtD7_I"


#from flask.ext.sqlalchemy import SQLAlchemy
#from werkzeug import generate_password_hash, check_password_hash

#db = SQLAlchemy()

#class User(db.Model):
  __tablename__ = 'Events'
  Event_id = db.Column(db.Integer, primary_key = True)
  Event_title = db.Column(db.String(100))
  Event_start = db.Column(db.String(100))
  Event_end = db.Column(db.String(100))
  GroupName = db.Column(db.String(100))
  GroupColor = db.Column(db.String(100))


 # def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password) '''

