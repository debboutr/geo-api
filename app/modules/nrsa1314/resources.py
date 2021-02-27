# encoding: utf-8
import sqlite3

from flask_restx import Namespace, Resource, abort, fields
from geojson import Feature, FeatureCollection
from geojson import Point as Geoj_point

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
                lon_dd83,
                lat_dd83
            from nrsa1314_allcond
            limit 3;
            """
        cursor = connR.execute(query)
        results = cursor.fetchall()

        points = []
        for item in results:
            site_no, date, lon, lat = item
            dd = Feature(
                properties=dict(site_id=site_no, date_collected=date),
                geometry=Geoj_point((float(lon), float(lat))),
            )
            points.append(dd)

        return FeatureCollection(points)


@api.route("/site/watersheds/<int:site_id>")
class Watersheds(Resource):
    def get(self):
        """
        Return a watershed for a given site.
        """
        connR = sqlite3.connect("/home/rick/testes.sqlite3")
        connR.enable_load_extension(True)
        connR.execute("SELECT load_extension('mod_spatialite')")

        query = """
            select site_no,
                st_x(geom),
                st_y(geom),
                st_geomfromtext("Point({lon} {lat})") as pt
            from all_sites
            limit 3;
            """
        cursor = connR.execute(query)
        results = cursor.fetchall()

        # print(results)

        points = []
        for item in results:
            site_no, x, y, _ = item
            props = {"site_no": f"{site_no}"}
            pnt_feature = Feature(
                id=f"{site_no}", geometry=Geoj_point((x, y)), properties=props
            )
            points.append(pnt_feature)

        from pprint import pprint

        print(FeatureCollection(points))
        return jsonify(FeatureCollection(points))
