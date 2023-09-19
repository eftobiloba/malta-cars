from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c2a0a038ba19d232295a58bd'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

from carMarket import routes
from carMarket import models