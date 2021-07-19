from flask import render_template, request,abort, flash
from sqlalchemy.exc import IntegrityError
from . import users
from .forms import RegisterForm
from .models import User
from app import db

from mod_users import forms

@users.route('/register/',methods=['POST',"GET"])
def register ():
    form = RegisterForm(request.form)
        
    if request.method == 'POST':
        user = User()
        if not form.validate_on_submit():
            return render_template('users/register.html', form = form)

        if form.password.data != form.confirm_password.data:
            error_message ='password and confirm password are not match'
            form.password.errors.append(error_message)
            return render_template('users/register.html', form = form)


        old_user =User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user : 
            flash('-------')
            return render_template('users/register.html', form = form)


        user.full_name = form.full_name.data
        user.email = form.email.data
        user.set_password(str(form.password.data))
        
        try :
            db.session.add(user)
            db.session.commit()
            flash('you create your account sucssesfully')
        except IntegrityError:
            db.session.rollback()
            flash('email is inused')
        
    return render_template('users/register.html', form = form)