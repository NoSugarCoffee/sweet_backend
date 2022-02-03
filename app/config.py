import os


class BaseConfig(object):
    PROJECT = "sweet_backend"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    BASE_URL = "https://yourdomain-flaskstarter.domain"
    ADMIN_EMAILS = ['admin@flaskstarter.domain']

    DEBUG = False
    TESTING = False

    SECRET_KEY = 'always-change-this-secret-key-with-random-alpha-nums'


class DefaultConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BaseConfig.PROJECT_ROOT + '/db.sqlite'
