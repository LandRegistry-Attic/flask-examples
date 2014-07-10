from flask import render_template
from appname import app, db
from  models import Foo
from flask.ext.assets import Environment, Bundle

# Static assets
assets = Environment(app)
css_main = Bundle(
    'stylesheets/main.scss',
    filters='scss',
    output='build/main.css',
    depends="**/*.scss"
)
assets.register('css_main', css_main)

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
    return {'asset_path': '/static/govuk_template/'}

@app.route('/')
def index():
    return render_template("index.html")

#  Some useful headers to set to beef up the robustness of the app
# https://www.owasp.org/index.php/List_of_useful_HTTP_headers
@app.after_request
def after_request(response):
    response.headers.add('Content-Security-Policy', "default-src 'self'")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
