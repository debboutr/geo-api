import json

from flask_restx import Namespace, Resource, abort, fields
from geojson import Feature, FeatureCollection, Point

from api.db import get_db
from api.utils.tolerance import find_tolerance

from api.models import (
    points_feature,
    detail_0405_point_feature,
    linestring_feature,
    polygon_feature,
    multipolygon_feature,
)

ns = Namespace(
    "NRSA 2004-05",
    description=(
        "data collected from survey sites in the [National Aquatic "
        "Resource Survey 2004-05]"
        "(https://www.epa.gov/national-aquatic-resource-surveys/"
        "wadeable-streams-assessment)"
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
            from sites_0405;
            """
        cursor = db.execute(query)
        results = cursor.fetchall()

        points = []
        for item in results:
            row = dict(item)
            dd = Feature(
                geometry=Point((float(row.pop("LON_DD")), float(row.pop("LAT_DD")))),
                properties=row,
            )
            points.append(dd)

        return FeatureCollection(points)


@ns.route("/point/<string:site_id>")
class Site(Resource):
    @ns.marshal_with(detail_0405_point_feature)
    def get(self, site_id):
        """
        Return PointFeature with all attributes and bbox of a single site from the survey
        """
        db = get_db()

        query = """
            select *
            from sites_0405
            where site_id='{site}';
            """
        result = db.execute(query.format(site=site_id.strip())).fetchone()

        if not result:
            abort(422, "Site ID does not exist in this survey")
        row = dict(result)
        point = Feature(
            geometry=Point((float(row["LON_DD"]), float(row["LAT_DD"]))),
            properties=row,
        )

        return point


@ns.route("/watersheds/<string:site_id>")
class Watersheds(Resource):
    @ns.marshal_with(polygon_feature)
    def get(self, site_id):
        """
        Return a watershed for a given site.
        """
        db = get_db()

        query = """
                select AsGeoJSON(geom) as wshed
                from watersheds_0405
                where site_id='{site}'
            """
        result = db.execute(query.format(site=site_id)).fetchone()
        if not result:
            abort(422, "Site ID does not exist in this survey")
        row = dict(result)
        poly = json.loads(row["wshed"])
        return Feature(geometry=poly)


@ns.route("/watershed/extent/<string:site_id>")
class Extent(Resource):
    @ns.marshal_with(polygon_feature)
    def get(self, site_id):
        """
        Return a watershed for a given site.
        """
        db = get_db()

        query = """
                select AsGeoJSON(Extent(geom)) as wshed
                from watersheds_0405
                where site_id='{site}'
            """
        result = db.execute(query.format(site=site_id)).fetchone()
        if not result:
            abort(422, "Site ID does not exist in this survey")
        poly = json.loads(dict(result)["wshed"])

        return Feature(geometry=poly)
