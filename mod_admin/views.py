from flask import session, render_template, request, abort
from werkzeug.security import check_password_hash
from . import admin
from app import db
from mod_users.models import User
from mod_users.forms import Login_form



@admin.route('/')
def index():
    return 'here id dmin page'

@admin.route('/login',methods=['POST','GET'])
def login():
    form = Login_form(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit :
            abort(400)
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        if not user :
            return 'incorrect credential' ,400
        if not user.check_password(form.password.data):
            return 'incorrect credential'
        session['email']= user.email
        session ['id'] =user.id
        return 'loged sucssecfully'
    if session.get('email') is not None:
        return 'you have already login'
    return render_template('admin/login_template.html',form = form)