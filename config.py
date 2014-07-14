import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///notforprod.db')
    # if using WTF forms you'll want some thing like this below§
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get('SESSION_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:test.db'
