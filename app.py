import flask.ext.restless as rest

from flask import Flask
from readme.model import Recommendation
from readme.db import session

app = Flask(__name__)
manager = rest.APIManager(app, session=session)
recommendation_blueprint = manager.create_api(
    Recommendation,
    methods=['GET', 'POST', 'PUT', 'DELETE']
)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8888,
        debug=True
    )
