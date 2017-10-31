from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__init__)

app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/ckwok_000/Desktop/Camperplus/login.db'
app.config['SECRET_KEY'] = 'camper+'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init.app(app)

class user(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.COlumn(String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route('/')
def index():
	user = User.query.filter_by(username='Kwok').first()
	login_user(user)
	return 'You are now logged in'

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return 'You are now logged out'

@app.route('/home')
@login_required
def home():
	return 'The current user is ' + current_user.username

if __init__ == '__main__':
	app.run(debug=True)