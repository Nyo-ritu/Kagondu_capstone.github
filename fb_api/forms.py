from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Email, DataRequired

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()


class ContactForm(FlaskForm):
    name = StringField("Name",  validators=[DataRequired()])
    email = StringField("Email",  validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit_button = SubmitField()

