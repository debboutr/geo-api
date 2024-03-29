from flask_restx import Api

from api.models import ns as models

from .epa import ns as epa
from .nlcd import ns as nlcd
from .nrsa0405 import ns as nrsa0405
from .nrsa0809 import ns as nrsa0809
from .nrsa1314 import ns as nrsa1314

api_v1 = Api(
    version="0.4.7",
    title="GeoAPI for National Aquatic Resource Surveys",
    description=(
        "This is a [FLASK-RESTX](https://flask-restx.readthedocs.io/en/latest/)"
        " powered API that is used to power visualizations in this "
        "[vuejs project](http://nars.debbout.info)!.\n\n"
        "Here is a link to the EPA's National Aquatic Resource Survey data "
        "[NARS](https://www.epa.gov/national-aquatic-resource-surveys)\n\n"
        "Source code on [GitHub](https://github.com/debboutr/geo-api)\n"
    ),
)

api_v1.add_namespace(models)
api_v1.add_namespace(nrsa0405, path="/nrsa0405")
api_v1.add_namespace(nrsa0809, path="/nrsa0809")
api_v1.add_namespace(nrsa1314, path="/nrsa1314")
api_v1.add_namespace(epa, path="/epa")
api_v1.add_namespace(nlcd, path="/nlcd")
