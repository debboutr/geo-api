from flask import Flask
from .endpoints import blueprint


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(blueprint, url_prefix="/api")
    app.config.from_pyfile("settings.py")
    app.config['RESTX_MASK_SWAGGER'] = False

    from . import db

    db.init_app(app)

    return app
