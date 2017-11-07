"""
Camper+ Web Application
"""

from flask import Flask

app = Flask(__name__)
import camperapp.routes
