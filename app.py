from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config  import Development,Production



app = Flask (__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'hi'

from mod_admin import admin 
from mod_users import users
app.register_blueprint(admin)
app.register_blueprint(users)