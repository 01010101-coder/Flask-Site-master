from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


App = Flask(__name__)
App.config.from_object(Configuration)
db = SQLAlchemy(App)
migrate = Migrate(App, db)
login = LoginManager(App)

from app import routes, models, errors