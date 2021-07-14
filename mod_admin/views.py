from flask import session
from . import admin
from app import db




@admin.route('/')
def index():
    return 'here id dmin page'

@admin.route('/login')
def login():
    session['name']= 'Arash'
    db.session .add ()
    return session.get('name')