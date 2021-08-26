from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(
        label="Username:", validators=[DataRequired(), Length(min=2, max=30)]
    )
    email_address = StringField(label="Email:", validators=[DataRequired(), Email()])
    password1 = PasswordField(
        label="Password:", validators=[DataRequired(), Length(min=6)]
    )
    password2 = PasswordField(
        label="Confirm password:", validators=[DataRequired(), EqualTo("password1")]
    )
    submit = SubmitField(label="Create account")
