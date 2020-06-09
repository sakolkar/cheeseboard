from flask import Flask, g, current_app
import models
import logging
import os
import sys


def create_app(name):
    app = Flask(name)
    app.logger = logger
    return app

def init_app(app, debug=False):
    app.debug = debug
    from .api import Api
    app.register_blueprint(Api(app.logger))
    app.db_engine = models.db(os.environ['DATABASE_URL'])


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
app = create_app(name=__name__,)

@app.before_request
def before_request():
    g.db_session = models.session(current_app.db_engine)

@app.teardown_appcontext
def teardown_request(exception=None):
    if hasattr(g, 'db_session'):
        g.db_session.remove()
