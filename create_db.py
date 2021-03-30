#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:44:26 2021

Gather files in this directory to make spatialite database tables. Future plans
to perform simplification of watershed geometries will also happen here. Tried
to load into a gpkg file, but the same queries are not available,i.e. AsGeoJSON

@author: rick
"""

import os
import sqlite3
import pandas as pd
import geopandas as gpd
import shapely.wkb as swkb
from shapely.geometry import Polygon, MultiPolygon, Point

DB_PATH = os.path.join(os.getcwd(), "geo.db")


def reduce_multi_poly(geom):
    """
    Find the largest polygon in GeometrySequence and return only the largest,
    to make the series Polygon only and not MultiPolygon.
    """
    if type(geom) == Polygon:
        return geom
    if type(geom) == MultiPolygon:
        areas = [g.area for g in geom.geoms]
        max_val = max(areas)
        max_idx = areas.index(max_val)
        return geom.geoms[max_idx]


def noholes(geom):
    return Polygon(geom.exterior.coords)


def make_records(gdf, pk="SITE_ID"):
    """
    Create tuples of WKB strings associated with primary key.
    """
    records = [
        {pk: gdf[pk].iloc[i], "wkb": swkb.dumps(gdf.geometry.iloc[i])}
        for i in range(gdf.shape[0])
    ]
    return tuple((d["wkb"], d[pk]) for d in records)


def reduce_geoms(geom):
    ring_count = len(geom.exterior.coords)
    if ring_count > 400_000:
        return geom.simplify(1000)
    elif ring_count > 20_000:
        return geom.simplify(500)
    elif ring_count > 5_000:
        return geom.simplify(100)
    else:
        return geom.simplify(30)


def force_geom_type(geom, ftype=MultiPolygon):
    if type(geom) != ftype:
        return ftype([geom])
    else:
        return geom


def load_db(gdf, tablename="watersheds_1314", pk="SITE_ID", geom_type="POINT"):

    # Drop all geospatial data
    df = gdf.drop(["geometry"], axis=1).set_index(pk)
    gdf = gdf[[pk, "geometry"]]
    tuples = make_records(gdf, pk=pk)
    # Create the table and populate it with non-geospatial datatypes
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(tablename, conn, if_exists="replace", index=True)
        conn.enable_load_extension(True)
        conn.load_extension("mod_spatialite")
        conn.execute("SELECT InitSpatialMetaData(1);")
        conn.execute(
            """
            SELECT AddGeometryColumn(?, 'geom', 3857, ?);
            """,
            (tablename, geom_type),
        )
        conn.executemany(
            f"""
            UPDATE {tablename}
            SET geom=GeomFromWKB(?, 3857)
            WHERE {tablename}.{pk} = ?
            """,
            (tuples),
        )


def main():
    # -- files --
    surveys = [
        dict(
            year="0405",
            latlon=("LAT_DD", "LON_DD"),
            sites="NRSA/2004/AAA_SITEINFO_CLEANED.csv",
            watersheds="NRSA/2004/wsashapefile_0/Streams2004_2005_Watersheds.shp",
        ),
        dict(
            year="0809",
            latlon=("LAT_DD83", "LON_DD83"),
            sites="NRSA/200809/siteinfo_0.csv",
            watersheds="NRSA/200809/NRSA0809_Watersheds.shp",
        ),
        dict(
            year="1314",
            latlon=("LAT_DD83", "LON_DD83"),
            sites="NRSA/201314/nrsa1314_allcond_05312019_0.csv",
            watersheds="NRSA/201314/watersheds_1314.shp",
        ),
    ]

    for survey in surveys:

        print("running...", survey["year"])
        lat, lon = survey["latlon"]
        watersheds = gpd.read_file(survey["watersheds"])
        sites = pd.read_csv(survey["sites"])

        sites["DATE_COL"] = pd.to_datetime(sites["DATE_COL"])
        sites = sites.sort_values("DATE_COL").drop_duplicates("SITE_ID")
        mgd = pd.merge(watersheds, sites[["SITE_ID"]], on="SITE_ID")

        mgd.geometry = (
            mgd.geometry.apply(reduce_multi_poly).apply(noholes).apply(reduce_geoms)
        )
        #    mgd["ext_count"] = mgd.geometry.apply(lambda x: len(x.exterior.coords))
        sites = sites.loc[sites.SITE_ID.isin(mgd.SITE_ID)]
        geometry = [Point(xy) for xy in zip(sites[lon], sites[lat])]
        points = gpd.GeoDataFrame(sites, crs="epsg:4269", geometry=geometry)
        load_db(
            points.to_crs("epsg:3857"),
            tablename=f"sites_{survey['year']}",
            geom_type="POINT",
        )
        load_db(
            mgd.to_crs("epsg:3857"),
            tablename=f"watersheds_{survey['year']}",
            geom_type="POLYGON",
        )

    mgd = gpd.read_file("NRSA/EPA_Regions/EPA_Regions.shp")
    mgd.geometry = mgd.geometry.apply(force_geom_type)
    load_db(
        mgd.to_crs("epsg:3857"),
        tablename="epa_regions",
        geom_type="MULTIPOLYGON",
        pk="EPAREGION",
    )


if __name__ == "__main__":
    main()

##############################################################################
#
# mgd.geometry = mgd.geometry.apply(reduce_geoms)
# mgd["ext_count2"] = mgd.geometry.apply(lambda x: len(x.exterior.coords))
# mgd["diff_count"] = abs(mgd.ext_count - mgd.ext_count2)
# bb = mgd.drop("geometry", axis=1)
#
#
#
#
## -- try gpkg -- FAIL
# points.to_file("package.gpkg", layer='sites_0809', driver="GPKG")
# mgd.to_crs("epsg:3857").to_file("package.gpkg", layer='watersheds_0809', driver="GPKG")
## -- trimming --
# mgd.loc[mgd.SITE_ID=="FW08NV039"].ext_count
# mgd.loc[mgd.SITE_ID=="FW08NV039"].Area_SqKM
# mgd.sort_values("ext_count", ascending=False).head(12)
# mgd.sort_values("ext_count").head(12)
# mgd.loc[mgd.ext_count>40000].sort_values("ext_count").head(12)
#
# f"""
# UPDATE {year}
# SET geom=GeomFromWKB(?, 3857)
# WHERE watersheds_{year}.site_id = ?
# """
#
#
# bb = mgd.drop("geometry", axis=1).sort_values("ext_count", ascending=False).head(247)
#
# area = "AREASQKM"
# area = "Area_SqKM"
# mgd.loc[mgd[area] > 10000]
# mgd.sort_values("Area_SqKM", ascending=False)
# mgd.sort_values(area, ascending=False).loc[mgd[area] > 10000]
# watersheds.sort_values(area, ascending=False).loc[watersheds[area] > 10000]
#
# geom = mgd.loc[mgd.SITE_ID == "FW08LA035"].geometry # largest
# geom = mgd.loc[mgd.SITE_ID == "FW08FL029"].geometry # around 10000
## -- 0809 --
# geom = mgd.iloc[598].geometry # 93_000 coords
# geom = mgd.iloc[302].geometry # 4251 coords
# geom = mgd.iloc[131].geometry # 50_000 coords
# geom = mgd.iloc[69].geometry # 20_000 coords
# geom = mgd.iloc[1032].geometry # 10_000 coords -- break from 500 -> 100
## -- 1314 --
# geom = mgd.iloc[1273].geometry # 569_785 coords
# geom = mgd.iloc[302].geometry # 4251 coords
# geom = mgd.iloc[131].geometry # 50_000 coords
# geom = mgd.iloc[69].geometry # 20_000 coords
# geom = mgd.iloc[985].geometry # 10_000 coords -- break from 500 -> 100
# geom = mgd.iloc[202].geometry # 10_000 coords -- break from 500 -> 100
# geom = mgd.iloc[168].geometry # 10_000 coords -- break from 500 -> 100
#
#
# len(geom.exterior.coords)
# simp = geom.simplify(30)
# simp = geom.simplify(100)
# simp = geom.simplify(500)
# simp = geom.simplify(1000)
# len(simp.exterior.coords)
#
#
# mgd.geometry = mgd.geometry.apply(reduce_geoms)
#
# gpd.GeoDataFrame(geometry=[geom], crs="epsg:5070").to_file("junk.shp")
# gpd.GeoDataFrame(geometry=[simp], crs="epsg:5070").to_file("junk2.shp")
#
#
# aa = gpd.read_file("junk.shp")
