class LoginForm(Form):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Login')