# encoding: utf-8
"""
Example RESTful API Server.
"""
from flask import g
from flask import Flask
from flask_restx import Api

api_v1 = Api(
    version="1.0",
    title="NARS | FLASK-RESTPlus GeoAPI for the NARS Survey 2018",
    description=(
        "This is a [FLASK-RESTX](https://flask-restx.readthedocs.io/en/latest/)"
        " powered API that is used to power visualizations in a coming vuejs project!.\n\n"
        "Source code on [GitHub](https://github.com/debboutr/geo-api)\n"
    ),
)


def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    # Initialize the Flask-App
    # app: Flask = Flask(__name__, **kwargs)
    app = Flask(__name__)

    # Load the config file
    app.config.from_object("config.DevelopmentConfig")

    # Initialize FLASK-RESTPlus
    api_v1.init_app(app)

    # Initialize the modules
    from . import modules

    modules.init_app(app)

    return app
