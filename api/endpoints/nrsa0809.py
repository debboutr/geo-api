import json

from flask_restx import Namespace, Resource, abort, fields
from geojson import Feature, FeatureCollection, Point

from api.db import get_db
from api.utils.tolerance import find_tolerance

from api.models import points_feature, detail_0809_point_feature, linestring_feature

ns = Namespace(
    "NRSA 2008-09",
    description=(
        "data collected from survey sites in the [National Aquatic "
        "Resource Survey 2008-09]"
        "(https://www.epa.gov/national-aquatic-resource-surveys/"
        "national-rivers-and-streams-assessment-2008-2009-results)"
    ),
)


@ns.route("/points/")
class Sites(Resource):
    @ns.marshal_with(points_feature)
    def get(self):
        """
        Return PointsFeature of all the sites from the survey
        """
        db = get_db()

        query = """
            select *
            from sites_0809
            limit 900;
            """
        cursor = db.execute(query)
        results = cursor.fetchall()

        points = []
        for item in results:
            row = dict(item)
            dd = Feature(
                geometry=Point(
                    (float(row.pop("LON_DD83")), float(row.pop("LAT_DD83")))
                ),
                properties=row,
            )
            points.append(dd)

        return FeatureCollection(points)


@ns.route("/point/<string:site_id>")
class Site(Resource):
    @ns.marshal_with(detail_0809_point_feature)
    def get(self, site_id):
        """
        Return PointFeature with all attributes and bbox of a single site from the survey
        """
        db = get_db()

        query = """
            select *
            from sites_0809
            where site_id='{site}';
            """
        result = db.execute(query.format(site=site_id.strip())).fetchone()

        if not result:
            abort(422, "Site ID does not exist in this survey")
        row = dict(result)
        point = Feature(
            geometry=Point((float(row.pop("LON_DD83")), float(row.pop("LAT_DD83")))),
            properties=row,
        )

        return point


@ns.route("/watersheds/<string:site_id>")
class Watersheds(Resource):
    @ns.marshal_with(linestring_feature)
    def get(self, site_id):
        """
        Return a watershed for a given site.

        all sites above 10_000 should use .005
        break below simplify at 10_000 @ 0.002
        break simplify below at 1_000 @ 0.001
        break NO simplify below at 500
        IAS9-0922_100 -- 0.8 sec --size 195054
        NDLS-1064_500 -- 0.8 sec -- size 439827
        TXR9-0916_20_000 -- 0.8 --size 141454
        NERM-1001_1_000_000 -- 0.97  -- size 542400
        LARM-1002_biggest -- 1.13  -- size 935138
        """
        db = get_db()

        query = """
                select area_sqkm
                from watersheds_0809
                where site_id='{site}'
            """
        result = db.execute(query.format(site=site_id)).fetchone()
        print(result)
        if not result:
            abort(422, "Site ID does not exist in this survey")

        tolerance = find_tolerance(result[0])

        spatial_function = (
            # simplifying geom if area_sqkm > 1_000
            f"AsGeoJSON(Simplify(ExteriorRing(geom), {tolerance}))"
            if tolerance
            else "AsGeoJSON(ExteriorRing(geom))"
        )

        query = """
                select {spatial_function} as wshed
                from watersheds_0809
                where site_id='{site}'
            """
        result = db.execute(
            query.format(spatial_function=spatial_function, site=site_id)
        ).fetchone()
        poly = json.loads(result[0])

        # return FeatureCollection([Feature(geometry=poly)])
        return Feature(geometry=poly)


@ns.route("/watershed/extent/<string:site_id>")
class Extent(Resource):

    # @ns.marshal_with(polygon_feature)
    def get(self, site_id):
        """
        Return a watershed for a given site.
        """
        db = get_db()

        query = """
                select AsGeoJSON(Extent(geom)) as wshed
                from wsheds_single_poly
                where site_id='LARM-1002'
            """
        # cursor = db.execute(query.format(site=site_id))
        result = db.execute(query).fetchone()
        poly = json.loads(result[0])

        return FeatureCollection([Feature(geometry=poly)])
