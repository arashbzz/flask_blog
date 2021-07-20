from os import error
import re
from flask import session, render_template, request, abort, flash,redirect,url_for
from werkzeug.security import check_password_hash
from . import admin
from app import db
from mod_users.models import User
from mod_users.forms import Login_form
from .utils import admin_only_viwe


@admin.route('/')
@admin_only_viwe
def index():
    return render_template('/admin/index.html')

@admin.route('/login',methods=['POST','GET'])
def login():
    form = Login_form(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit :
            abort(400)
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        if not user :
            flash('incorrect credential', 'error')
            return  render_template('admin/login_template.html',form = form)
        if not user.check_password(form.password.data):
            
            flash('incorrect credential', 'error')
            return  render_template('admin/login_template.html',form = form)
        if not user.is_user_admin():
            flash('you are not admin', 'error')
            return  render_template('admin/login_template.html',form = form)
        session['email']= user.email
        session ['id'] =user.id
        session['role'] = user.role
        print (session)
        return redirect(url_for('admin.index'))
    if session.get('role') ==1:
        return redirect(url_for('admin.index'))
    return render_template('admin/login_template.html',form = form)

@admin.route('/logout')
@admin_only_viwe
def logout():
    session.clear()
    flash ('you logout successfully.', 'warning')
    return redirect (url_for('admin.login'))