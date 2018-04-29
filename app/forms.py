from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField,SelectField
from wtforms.validators import InputRequired,DataRequired,Email
from flask_wtf.file import FileAllowed, FileRequired, FileField


class LoginForm(FlaskForm):
    firstname=StringField('First Name', validators=[DataRequired('Please enter a firstname')])
    lastname=StringField('Last Name', validators=[DataRequired('Please enter a lastname')])
    email=StringField('Email Address', validators=[Email(message='This is not a valid email'), DataRequired('Please provide an email address')])
    location=StringField('Location', validators=[DataRequired('Please enter a location')])
    biography=TextAreaField('Biography', validators=[DataRequired('Please enter a short biography')])
    gender=SelectField('Gender',choices=[('M','Male'),('F','Female'),('O','Other')],validators=[DataRequired('Select a gender')])
    photograph= FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'], 'Images only!')])
    