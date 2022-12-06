import json

from flask_restx import Namespace, Resource, abort
from geojson import Feature, FeatureCollection, Point

from api.db import get_db
from api.models import nlcd_feature, category_feature

ns = Namespace(
    "NLCD",
    description=(
        "data collected from survey sites in the [StreamCat database]"
        "(https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset)"
    ),
)


@ns.route("/<string:year>/<string:comid>/")
class Categories(Resource):
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

        result = db.execute(query.format(year=year, comid=comid)).fetchone()
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

@ns.route("/category/<string:comid>/<string:category>/")
class Category(Resource):
    @ns.marshal_with(category_feature)
    def get(self, comid, category):
        """
        Return all years of a single category on a given COMID
        """
        db = get_db()

        years = ["2001","2004","2006","2011","2013","2016","2019"]
        hold = {}
        for year in years:
            query = """
                select nlcd_{year}.{category}
                from nlcd_{year}
                where COMID={comid};
                """
            result = db.execute(query.format(year=year, comid=comid, category=category)).fetchone()
            hold[year] = result[category]
        if not hold:
            abort(422, "COMID does not exist in this survey")
        return hold
