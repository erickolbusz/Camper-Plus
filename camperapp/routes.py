"""Routes for Camper+ app."""

from camperapp import app


@app.route('/', methods=['GET'])
def index():
    """View displays the homepage"""
    return "<h1>Welcome To Camper+</h1>"
