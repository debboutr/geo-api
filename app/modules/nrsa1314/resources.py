# encoding: utf-8
import json
import sqlite3

from flask_restx import Namespace, Resource, abort, fields
from geojson import Feature, FeatureCollection
from geojson import Point as Geoj_point
from geojson import Polygon as Geoj_polygon

from app.modules.nrsa1314 import NRSA1314ApiNamespace

api = Namespace("nrsa1314", description=NRSA1314ApiNamespace.description)

point = api.model(
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

props = api.model(
    "Properties",
    {
        "site_id": fields.String(required=True),
        "basin_name": fields.String(required=True),
        "date_collected": fields.String(required=True),
    },
)

point_feature = api.model(
    "PointFeature",
    {
        "type": fields.String(required=True, default="Feature"),
        "properties": fields.Nested(props, required=True),
        "geometry": fields.Nested(point, required=True),
    },
)

points_feature = api.model(
    "PointsFeature",
    {
        "type": fields.String(required=True, default="FeatureCollection"),
        "features": fields.List(fields.Nested(point_feature, required=True)),
    },
)


polygon = api.model(
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

polygon_feature = api.model(
    "PolygonFeature",
    {
        "type": fields.String(default="Feature", require=True),
        "geometry": fields.Nested(polygon, required=True),
    },
)


@api.route("/site/points/")
class Sites(Resource):
    @api.marshal_with(points_feature)
    def get(self):
        """
        Return PointsFeature of all the sites from the survey
        """
        connR = sqlite3.connect("/home/rick/testes.sqlite3")

        query = """
            select site_id,
                date_col,
                maj_bas_nm,
                lon_dd83,
                lat_dd83
            from nrsa1314_allcond
            limit 900;
            """
        cursor = connR.execute(query)
        results = cursor.fetchall()

        points = []
        for item in results:
            site_no, date, basin_name, lon, lat = item
            dd = Feature(
                properties=dict(
                    site_id=site_no, basin_name=basin_name, date_collected=date
                ),
                geometry=Geoj_point((float(lon), float(lat))),
            )
            points.append(dd)

        return FeatureCollection(points)


@api.route("/site/watersheds/<string:site_id>")
class Watersheds(Resource):

    # @api.marshal_with(polygon_feature)
    def get(self, site_id):
        """
        Return a watershed for a given site.
        """
        connR = sqlite3.connect("/home/rick/testes.sqlite3")
        connR.enable_load_extension(True)
        connR.execute("SELECT load_extension('mod_spatialite')")

        query = """
                select AsGeoJSON(Simplify(geom, 0.002)) as wshed
                from wsheds_single_poly
                where site_id='MNR9-0909'
            """
        # cursor = connR.execute(query.format(site=site_id))
        cursor = connR.execute(query)
        results = cursor.fetchone()
        poly = json.loads(results[0])

        return FeatureCollection([Feature(geometry=poly)])
