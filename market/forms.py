from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label="Username:")
    email = StringField(label="Email:")
    password1 = PasswordField(label="Password:")
    password2 = PasswordField(label="Confirm password:")
    submit = SubmitField(label="Create account")
