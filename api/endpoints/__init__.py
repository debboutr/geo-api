from flask import Blueprint
from flask_restx import Api, fields

from api.models import ns as models

from .epa import ns as epa

# from .geoloo import ns as geo
from .nrsa0405 import ns as nrsa0405
from .nrsa0809 import ns as nrsa0809
from .nrsa1314 import ns as nrsa1314

blueprint = Blueprint("jerky", __name__)
api_v1 = Api(
    blueprint,
    version="0.4.7",
    title="GeoAPI for National Aquatic Resource Surveys and other water resources",
    description=(
        "This is a [FLASK-RESTX](https://flask-restx.readthedocs.io/en/latest/)"
        " powered API that is used to power visualizations in a coming vuejs project!.\n\n"
        "[NARS](https://www.epa.gov/national-aquatic-resource-surveys)\n\n"
        "Source code on [GitHub](https://github.com/debboutr/geo-api)\n"
    ),
)

api_v1.add_namespace(models)
api_v1.add_namespace(nrsa0405, path="/nrsa0405")
api_v1.add_namespace(nrsa0809, path="/nrsa0809")
api_v1.add_namespace(nrsa1314, path="/nrsa1314")
# api_v1.add_namespace(geo, path="/geo")
api_v1.add_namespace(epa, path="/epa")
