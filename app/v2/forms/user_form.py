from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignupForm(Flaskform):
    first_name = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=60)])
    last_name = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=60])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')