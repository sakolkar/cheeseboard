from flask import Flask
import logging


def create_app(name):
    app = Flask(name)
    app.logger = logger
    return app

def init_app(app, debug=False):
    app.debug = debug
    from .api import Api
    app.register_blueprint(Api())


logger = logging.getLogger(__name__)
app = create_app(name=__name__,)
