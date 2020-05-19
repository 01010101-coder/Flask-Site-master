import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "E1FE22BC394EE1FEADD233BB8C34C"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False