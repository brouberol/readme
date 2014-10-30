# -*- coding: utf-8 -*-

"""Definition and configuration of the Flask application."""

import flask.ext.restless as rest

from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

from readme.model import Recommendation
from readme.db import session
from readme import conf as c


app = Flask(__name__)

# Definition of the REST API over the database models
manager = rest.APIManager(app, session=session)
recommendation_blueprint = manager.create_api(
    Recommendation,
    methods=['GET', 'POST', 'PUT', 'DELETE']
)

# Definition of the static assets handler
assets = Environment(app)

# Definition of the JS assets pipeline
js_files = [c.JS_DIR + '/' + js for js in c.JS_FILES]
packed_js = c.JS_DIR + '/' + c.PACKED_JS
js = Bundle(
    *js_files,
    filters='jsmin',
    output=packed_js)
assets.register('js_all', js)

# Definition of the CSS assets pipeline
css_files = [c.CSS_DIR + '/' + css for css in c.CSS_FILES]
packed_css = c.CSS_DIR + '/' + c.PACKED_CSS
css = Bundle(
    *css_files,
    filters='cssmin',
    output=packed_css)
assets.register('css_all', css)


@app.route('/')
def index():
    return render_template('base.html.jinja2')
