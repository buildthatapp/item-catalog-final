import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

# Configure database
app = Flask(__name__)
app.config['SECRET_KEY'] = "b'c(\x18\xa3\xed,\xc4z\x9a7\x0c\x055\x15\xc2\xe5j\x9c\xd9w<\x90\xa7\x80'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'item_catalog.db')
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

import models
import views