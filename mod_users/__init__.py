from flask import Blueprint
from flask.helpers import url_for

users = Blueprint('users',__name__,url_prefix= '/users/')

from .models import User