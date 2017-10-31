"""Routes for Camper+ app."""

from camperapp import app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    """View displays the homepage"""
    return "<h1>Welcome To Camper+</h1>"

@app.route('/schedule', methods=['GET','POST'])
def schedule():
    """View displays the schedule-making page"""
    return render_template("schedule.html")
