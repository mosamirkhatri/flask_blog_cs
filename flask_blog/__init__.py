import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '1f02242ffa67ab227f54e9414a69cccc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_SENDER'] = os.environ.get('MAIL_SENDER_EMAIL')

app.config['MAIL_USERNAME'] = 'samir.khatri11'
# app.config['MAIL_DEFAULT_SENDER'] = 'samir.khatri11@yahoo.com'
app.config['MAIL_PASSWORD'] = 'aceraspire5742'
mail = Mail(app)

from . import routes