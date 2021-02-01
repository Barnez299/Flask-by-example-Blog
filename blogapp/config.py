import os
import app

basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    SECRET_KEY = 'secretkeys'
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456789@localhost:5432/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True




