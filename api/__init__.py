from flask import Flask
from .endpoints import blueprint

    # SWAGGER_UI_JSONEDITOR = True

def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(blueprint, url_prefix="/api")
    app.config['RESTX_MASK_SWAGGER'] = False

    return app
