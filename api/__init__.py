from flask import Flask
from .endpoints import blueprint


def create_app(config_file="../instance/settings.cfg"):

    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(blueprint)
    app.config.from_pyfile(config_file)
    app.config['RESTX_MASK_SWAGGER'] = False

    from . import db

    db.init_app(app)

    return app
