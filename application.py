"Temporary file to quickly run flask App in Debug Mode"

from camperapp import app

if __name__ == "__main__":
    app.run(debug=True)
