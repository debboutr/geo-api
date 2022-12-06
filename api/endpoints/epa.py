import json

from flask_restx import Namespace, Resource, abort, fields
from geojson import FeatureCollection, Feature

from api.db import get_db
from api.models import multipolygon_feature, polygon_feature, multipolygon_collection

ns = Namespace(
    "EPA Regions",
    description=(
        "EPA Region polygons collected from [GeoPlatform](https://hifld-geoplatform."
        "opendata.arcgis.com/datasets/c670540796584c72b4f59b676ccabe6a_3)"
    ),
)


@ns.route("/regions/")
class Regions(Resource):
    @ns.marshal_with(multipolygon_collection)
    def get(self):
        """
        Return all EPA regions in CONUS
        """
        db = get_db()

        query = """
            select EPAREGION,  AsGeoJSON(geom) as region
            from epa_regions;
            """
        cursor = db.execute(query)
        results = cursor.fetchall()

        regions = []
        for item in results:
            row = dict(item)

            dd = Feature(
                geometry=json.loads(row["region"]),
                properties=row,
            )
            regions.append(dd)
        print(regions[0].keys())
        print(regions[0]["geometry"].keys())
        print(FeatureCollection(regions).keys())
        print(FeatureCollection(regions)["features"][0].keys())

        return FeatureCollection(regions)


@ns.route("/region/<string:region_id>")
class Region(Resource):
    """there needs to be a message here"""

    @ns.marshal_with(polygon_feature)
    def get(self, region_id):
        """
        Return polygon of the EPA Region
        """
        db = get_db()

        query = """
            select EPAREGION,  AsGeoJSON(geom) as region
            from epa_regions
            where objectid='{oid}';
            """
        result = db.execute(query.format(oid=region_id.strip())).fetchone()

        if not result:
            abort(422, "Site ID does not exist in this survey")
        row = dict(result)
        poly = json.loads(row["region"])

        return Feature(geometry=poly, properties=row)
