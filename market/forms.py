from market.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class RegisterForm(FlaskForm):
    # Use validate_FIELDNAME function names
    # flask_wtf handles them automatically
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists!")

    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError("Email already exists!")

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


class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField(label="Log in")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell")
