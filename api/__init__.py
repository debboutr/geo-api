import os

from flask import Flask
from flask_cors import CORS

from api.endpoints import api_v1 as api


def create_app(config_file="../instance/settings.cfg"):

    app = Flask(__name__, instance_relative_config=True)
    api.init_app(app)
    app.config.from_pyfile(config_file)
    app.config["RESTX_MASK_SWAGGER"] = False

    CORS(app, resources={r"/*": {"Access-Control-Allow-Origin": "*"}})
    from . import db

    db.init_app(app)

    return app
