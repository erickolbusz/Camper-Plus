"""Google Calendar API configuration"""

api_key = "AIzaSyDfnLfxNeG45N_tBtUutrB9K6-GYCtD7_I"


from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
"""
will be lodified
db = SQLAlchemy()

class Parent(db.Model):
  __tablename__ = 'Parent'
  uid = db.Column(db.Integer, primary_key = True)
  GroupName = db.Column(db.String(100))
  GroupName = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)
"""

