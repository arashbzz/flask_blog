from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField , PasswordField
from wtforms.validators import DataRequired, Email 

class Login_form (FlaskForm):
    full_name =StringField('name')
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    role = StringField('role')
    submite = SubmitField('submite')

class RegisterForm(FlaskForm):
    full_name = StringField()
    email = EmailField(validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])