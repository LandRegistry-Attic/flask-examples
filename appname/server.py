from flask import render_template
from appname import app, db
from  models import Foo

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
    return {'asset_path': '/static/govuk_template/'}

@app.route('/')
def index():
    return render_template("landregistry_base.html")
