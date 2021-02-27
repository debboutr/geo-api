# encoding: utf-8
import sqlite3
import json

import geopy.distance
import pyproj
from app.modules.nrsa1314 import NRSA1314ApiNamespace
from flask import request, jsonify
from flask_restx import Namespace, Resource, abort
from flask_restx import fields, marshal
from functools import partial
from geopy import Point as GeopyPoint, distance
from http import HTTPStatus
from shapely.geometry import Polygon, LineString
from shapely.ops import transform
from geojson import Feature, FeatureCollection
from geojson import Point as Geoj_point


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
        "site_no": fields.Integer(required=True),
    },
)

point_feature = api.model(
    "PointFeature",
    {
        "id": fields.Integer(require=True),
        "type": fields.String(required=True, default="Feature"),
        "properties": fields.Nested(props, required=True),
        "geometry": fields.Nested(point, required=True),
    },
)


@api.route("/site/points/")
class Sites(Resource):
    @api.marshal_list_with(point_feature, envelope="FeatureCollection")
    def get(self):
        """
        Return all of the sites from the survey
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

        points = []
        for item in results:
            site_no, x, y, _ = item
            dd = dict(
                id=site_no,
                properties=dict(site_no=site_no),
                geometry=Geoj_point((x, y)),
            )
            points.append(dd)

        return points


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
