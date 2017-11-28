"""Camper+ Web Application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql+psycopg2://postgres:Zzz159357@localhost:5432/camper_plus"
=======
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://localhost/camper_plus"
>>>>>>> 3e956219e03aa18f70d76a37d44310d581b03107
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "0QZSIXW7U50133JZuZ6gpkwZ9yYCXY"
heroku = Heroku(app)
db = SQLAlchemy(app)
app.secret_key = "0QZSIXW7U50133JZuZ6gpkwZ9yYCXY"

import camperapp.routes
