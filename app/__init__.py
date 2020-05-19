from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

App = Flask(__name__)
App.config.from_object(Configuration)
db = SQLAlchemy(App, db)

from app import routes