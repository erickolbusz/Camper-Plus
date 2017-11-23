from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign in")


class SignupFormManager(Form):
    name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')


class ChildEnrollmentForm(Form):
    child_first_name = StringField('First name')
    child_last_name = StringField('Last name')
    child_birth_date = DateField('Birthday')
    child_grade = IntegerField('Grade')
    child_gender = SelectField('Gender', choices=['Male', 'Female'])
    medical_notes = TextAreaField('Medical Notes')

