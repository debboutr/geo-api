import json
import sqlite3

# from sqlalchemy import text # TODO use this for string substitution
from flask_restx import Namespace, Resource, abort, fields
from geojson import Feature, FeatureCollection, Point

from api.db import get_db


ns = Namespace(
    "nrsa1314",
    description=(
        "data collected from survey sites in the [National Aquatic "
        "Resource Survey 2013-14]"
        "(https://www.epa.gov/national-aquatic-resource-surveys/"
        "national-rivers-and-streams-assessment-2013-2014-results)"
    ),
)

point = ns.model(
    "PointGeometry",
    {
        "type": fields.String(required=True),
        "coordinates": fields.List(
            fields.Float,
            required=True,
            type="Array",
            default=[13.4197998046875, 52.52624809700062],
        ),
    },
)

props = ns.model(
    "Properties",
    {
        "site_id": fields.String(required=True),
        "basin_name": fields.String(required=True),
        "date_collected": fields.String(required=True),
    },
)

point_feature = ns.model(
    "PointFeature",
    {
        "type": fields.String(required=True, default="Feature"),
        "properties": fields.Nested(props, required=True),
        "geometry": fields.Nested(point, required=True),
    },
)

points_feature = ns.model(
    "PointsFeature",
    {
        "type": fields.String(required=True, default="FeatureCollection"),
        "features": fields.List(fields.Nested(point_feature, required=True)),
    },
)


polygon = ns.model(
    "PolygonGeometry",
    {
        "type": fields.String(required=True, default="Polygon"),
        "coordinates": fields.List(
            fields.List(fields.Float, required=True, type="Array"),
            required=True,
            type="Array",
            default=[
                [13.4197998046875, 52.52624809700062],
                [13.387527465820312, 52.53084314728766],
                [13.366928100585938, 52.50535544522142],
                [13.419113159179688, 52.501175722709434],
                [13.4197998046875, 52.52624809700062],
            ],
        ),
    },
)

polygon_feature = ns.model(
    "PolygonFeature",
    {
        "type": fields.String(default="Feature", require=True),
        "geometry": fields.Nested(polygon, required=True),
    },
)


linestring = ns.model(
    "LineStringGeometry",
    {
        "type": fields.String(required=True, default="LineString"),
        "coordinates": fields.List(
            fields.List(fields.Float, required=True, type="Array"),
            required=True,
            type="Array",
            default=[
                [13.420143127441406, 52.515594085869914],
                [13.421173095703125, 52.50535544522142],
                [13.421173095703125, 52.49532344352079],
            ],
        ),
    },
)

linestring_feature = ns.model(
    "LineStringFeature",
    {
        "type": fields.String(default="Feature", require=True),
        "geometry": fields.Nested(linestring, required=True),
    },
)


def find_tolerance(area):
    if area > 1_000_000:
        return "0.005"
    elif area > 10_000:
        return "0.002"
    elif area > 1_000:
        return "0.001"
    else:
        None


@ns.route("/site/points/")
class Sites(Resource):
    @ns.marshal_with(points_feature)
    def get(self):
        """
        Return PointsFeature of all the sites from the survey
        """
        db = get_db()

        query = """
            select site_id,
                date_col,
                maj_bas_nm,
                lon_dd83,
                lat_dd83
            from nrsa1314_allcond
            limit 900;
            """
        cursor = db.execute(query)
        results = cursor.fetchall()

        points = []
        for item in results:
            site_no, date, basin_name, lon, lat = item
            dd = Feature(
                properties=dict(
                    site_id=site_no, basin_name=basin_name, date_collected=date
                ),
                geometry=Point((float(lon), float(lat))),
            )
            points.append(dd)

        return FeatureCollection(points)


@ns.route("/site/point/<string:site_id>")
class Site(Resource):

    # @ns.marshal_with(points_feature)
    def get(self, site_id):
        """
        Return PointFeature with all attributes and bbox of a single site from the survey
        """
        db = get_db()

        query = """
            SELECT nrsa1314_allcond.site_id, nrsa1314_allcond.date_col, AsGeoJSON(Extent(wsheds_single_poly.geom))
            FROM nrsa1314_allcond
            INNER JOIN wsheds_single_poly
            ON nrsa1314_allcond.site_id=wsheds_single_poly.site_id and nrsa1314_allcond.site_id='{site}';
            """
        result = db.execute(query.format(site=site_id.strip())).fetchone()

        if not result:
            abort(422, "Site ID does not exist in this survey")
        print(result)

        return {"rick": 47}


@ns.route("/site/watersheds/<string:site_id>")
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
                from wsheds_single_poly
                where site_id='{site}'
            """
        result = db.execute(query.format(site=site_id)).fetchone()
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
                from wsheds_single_poly
                where site_id='{site}'
            """
        result = db.execute(
            query.format(spatial_function=spatial_function, site=site_id)
        ).fetchone()
        poly = json.loads(result[0])

        # return FeatureCollection([Feature(geometry=poly)])
        return Feature(geometry=poly)


@ns.route("/site/watershed/extent/<string:site_id>")
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
