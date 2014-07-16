import os, logging
from flask import Flask

app = Flask(__name__)

# to run the app set an environment variable called SETTINGS
# the value should be set to one of the classes in config.py
# e.g. export SETTINGS="config.TestConfig"
app.config.from_object(os.environ.get('SETTINGS'))

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

app.logger.info("\nConfiguration\n%s\n" % app.config)

# if this app uses a db you'll need this
# from flask.ext.sqlalchemy import SQLAlchemy
# db = SQLAlchemy(app)

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
    return {'asset_path': '/static/govuk_template/'}

