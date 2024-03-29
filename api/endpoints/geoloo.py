from functools import partial
from http import HTTPStatus

import geopy.distance
import pyproj
from flask import request
from flask_restx import Namespace, Resource, abort, fields
from geopy import Point as GeopyPoint
from geopy import distance
from shapely.geometry import LineString, Polygon
from shapely.ops import transform

ns = Namespace("workingonit")

bounding_box = ns.model(
    "BoundingBox",
    {
        "x_lat": fields.Float(),
        "y_lat": fields.Float(),
        "x_lng": fields.Float(),
        "y_lng": fields.Float(),
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

point = ns.model(
    "PointGeometry",
    {
        "type": fields.String(required=True, default="Point"),
        "coordinates": fields.List(
            fields.List(fields.Float, required=True, type="Array"),
            required=True,
            type="Array",
            example=[-108.4182, 36.75052],
        ),
    },
)

blue = ns.model(
    "Recko",
    {
        "site_id": fields.String(required=True),
        "basin_name": fields.String(required=True),
        "date_collected": fields.String(required=True),
    },
)


point_feature = ns.model(
    "DeadMansBluff",
    {
        "type": fields.String(default="Feature", require=True),
        "properties": fields.Nested(blue, required=True),
        "geometry": fields.Nested(point, required=True),
    },
)


@ns.route("/polygon/area/")
class PolygonArea(Resource):
    """
    Return the area of a polygon in m²
    """

    def get(self):
        pass

    # @ns.expect(polygon_feature, validate=True)
    @ns.doc(id="polygon_area")
    def post(self):
        """
        Return the area of a polygon in m²
        """

        try:
            # projection = partial(
            #     pyproj.transform,
            #     pyproj.Proj('epsg:4269'),
            #     pyproj.Proj('epsg:5070')
            # )

            projection = pyproj.Transformer.from_crs(
                pyproj.CRS("epsg:4326"), pyproj.CRS("epsg:5070"), always_xy=True
            ).transform

            return transform(
                projection, Polygon(request.json["geometry"]["coordinates"])
            ).area
        except Exception as err:
            abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="The GeoJSON polygon couldn't be processed.",
                error=err,
            )


@ns.route("/point/distance/")
@ns.param(
    "start_lat", "Latitude of the start point e.g. 52.52624809700062", _in="query"
)
@ns.param(
    "start_lng", "Longitude of the start point e.g. 13.4197998046875", _in="query"
)
@ns.param("end_lat", "Latitude of the end point e.g. 52.50535544522142", _in="query")
@ns.param("end_lng", "Longitude of the end point e.g. 13.366928100585938", _in="query")
class PointToPointDistance(Resource):
    """
    Return the distance in kilometers between two points.
    """

    # @ns.expect(point_feature)
    @ns.doc(id="point_to_point_distance")
    def get(self):
        """
        Return the distance in kilometers between two points.
        """
        if (
            request.args.get("start_lat", "")
            and request.args.get("start_lng", "")
            and request.args.get("end_lat", "")
            and request.args.get("end_lng", "")
        ):
            try:
                return geopy.distance.distance(
                    GeopyPoint(
                        longitude=request.args.get("start_lng", type=float),
                        latitude=request.args.get("start_lat", type=float),
                    ),
                    GeopyPoint(
                        longitude=request.args.get("end_lng", type=float),
                        latitude=request.args.get("end_lat", type=float),
                    ),
                ).km
            except Exception:
                pass

        abort(
            HTTPStatus.BAD_REQUEST,
            message="Please provide a valid query e.g. with the following url arguments: "
            "http://127.0.0.1:4000/api/geoapi/point/distance/?start_lng=8.83546&start_lat=53.071124&end_lng=10.006168&end_lat=53.549926",
        )


@ns.route("/linestring/length/")
class LinestringLength(Resource):
    """
    Return if the length in meter of a given GeoJSON LineString
    """

    # @ns.expect(linestring_feature, validate=True)
    @ns.doc(id="linestring_length")
    def post(self):
        """
        Return if the length in meter of a given GeoJSON LineString
        """
        try:
            line_coordinates = request.json["geometry"]["coordinates"]
            length = 0
            for idx in range(len(line_coordinates) - 1):
                length += distance.distance(
                    line_coordinates[idx], line_coordinates[idx + 1]
                ).meters
            return length
        except Exception as err:
            pass
        abort(
            HTTPStatus.BAD_REQUEST,
            message="Please provide a valid POST GeoJSON and valid query with the following url arguments.",
        )
