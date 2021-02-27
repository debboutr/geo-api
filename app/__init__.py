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
        "This is a FLASK-RESPlus powered API with geospatial super power.\n\n"
        "Checkout more at https://gis-ops.com or https://github.com/gis-ops\n"
    ),
)


def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    # Initialize the Flask-App
    app: Flask = Flask(__name__, **kwargs)

    # Load the config file
    app.config.from_object("config.DevelopmentConfig")

    DATABASE = "/home/rick/testes.sqlite3"

    def get_db():
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()

    # Initialize FLASK-RESTPlus
    api_v1.init_app(app)

    # Initialize the modules
    from . import modules

    modules.init_app(app)

    return app
