from appname import app, db
from  models import Foo

@app.route('/')
def index():
    return "this is the index"
