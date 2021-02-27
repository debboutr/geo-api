# encoding: utf-8


class BaseConfig(object):
    ENABLED_MODULES = {
        "api",
        # 'geoapi',
        "nrsa1314",
    }

    SWAGGER_UI_JSONEDITOR = True
    RESTX_MASK_SWAGGER = False


class DevelopmentConfig(BaseConfig):
    """config for DevelopmentConfig."""

    DEBUG = False
    DEVELOPMENT = True
