from mod_admin import views
from flask import Blueprint

blog = Blueprint('blog',__name__,url_prefix='/blog/')

from . import models, views
from mod_blog.views import index