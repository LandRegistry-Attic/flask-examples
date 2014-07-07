import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///notforprod.db')
    # If DATABASE_URL not set fall back to sqlite db

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'a very secret thing indeed'

class HerokuConfig(Config):
    # db config from Config will do, but set any other env vars
    # specific to heroku here
    pass

class DevelopmentConfig(Config):
    # use this for local dev in fig+docker world
    DEBUG = True

    # env vars in this context have their own naming convention
    # assuming an image called 'db' in the fig.yml you are using and a link
    # to that db image from the flask app override default
    # also assumes we're using something based on orchard/postgres
    # image that creates a user, password and db called docker
    # that can be over ridden from fig.yml
    URI = os.environ.get('DB_1_PORT_5432_TCP', '').replace('tcp://', '')
    DB = os.environ.get('POSTGRESQL_DB')
    USER = os.environ.get('POSTGRESQL_USER')
    PASS = os.environ.get('POSTGRESQL_PASS')

    # format is dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s/%s" %  (USER, PASS, URI, DB)


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:test.db'
