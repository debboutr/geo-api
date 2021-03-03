from flask import Blueprint
from flask_restx import Api

from .nrsa import ns as nrsa
from .geoloo import ns as geo

blueprint = Blueprint("jerky", __name__)
api_v1 = Api(
    blueprint,
    version="4.7",
    title="FLASK-RESTX GeoAPI for NARS and other water resources",
    description=(
        "This is a [FLASK-RESTX](https://flask-restx.readthedocs.io/en/latest/)"
        " powered API that is used to power visualizations in a coming vuejs project!.\n\n"
        "[NARS](https://www.epa.gov/national-aquatic-resource-surveys)\n\n"
        "Source code on [GitHub](https://github.com/debboutr/geo-api)\n"
    ),
)

api_v1.add_namespace(nrsa, path="/nrsa")
api_v1.add_namespace(geo, path="/geo")
