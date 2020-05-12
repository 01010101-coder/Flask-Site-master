from flask import Flask
from config import Configuration


App = Flask(__name__)
App.config.from_object(Configuration)


from app import routes