from mod_blog.models import Category
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, TextAreaField, TextField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email


class CreateBlog (FlaskForm):
    title = TextField('name', validators=[DataRequired()])
    summery = TextAreaField('descriptiom')
    content = TextAreaField('content', validators=[DataRequired()])
    slug = TextField('slug', validators=[DataRequired()])
    categry = SelectMultipleField(choices=[1, 2])
