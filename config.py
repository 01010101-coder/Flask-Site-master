import os

class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "E1FE22BC394EE1FEADD233BB8C34C"