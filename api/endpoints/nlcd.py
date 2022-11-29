import json

from flask_restx import Namespace, Resource, abort
from geojson import Feature, FeatureCollection, Point

from api.db import get_db
from api.models import nlcd_feature

ns = Namespace(
    "NLCD",
    description=(
        "data collected from survey sites in the [StreamCat database]"
        "(https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset)"
    ),
)


@ns.route("/<string:year>/<string:comid>/")
class Sites(Resource):
    @ns.marshal_with(nlcd_feature)
    def get(self, year, comid):
        """
        Return NLCD  Watershed data of given COMID
        """
        db = get_db()

        query = """
            select *
            from nlcd_{year}
            where COMID={comid};
            """
        print(query.format(year=year, comid=comid))

        result = db.execute(query.format(year=year, comid=comid)).fetchone()
        print(result)
        print(dict(result))
        d = dict(result)
        if not result:
            abort(422, "COMID does not exist in this survey")

        base = {
            k: d[k] for k in d if k in ["SITE_ID", "COMID", "WsAreaSqKm", "WsPctFull"]
        }
        categories = {k: d[k] for k in d if k.startswith("Pct")}
        base["categories"] = categories

        # poly = json.loads(row["wshed"])
        return base
