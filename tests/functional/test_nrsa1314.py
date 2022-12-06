import json


def test_1314_points(client):

    response = client.get("/nrsa1314/points/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert list(data.keys()) == ["type", "features"]
    assert data["type"] == "FeatureCollection"
    assert type(data["features"]) == list
    assert len(data["features"]) == 1852
    feature = data["features"][0]
    assert list(feature.keys()) == ["type", "properties", "geometry"]
    assert feature["type"] == "Feature"
    assert list(feature["properties"].keys()) == [
        "SITE_ID",
        "COMID",
        "DATE_COL",
        "YEAR",
        "WSAREASQKM",
        "VISIT_NO",
    ]


def test_1314_site_detail(client):

    site_id = "AZR9-0903"
    response = client.get(f"/nrsa1314/point/{site_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert list(data.keys()) == ["type", "geometry", "properties"]
    assert data["type"] == "Feature"
    assert list(data["geometry"].keys()) == ["type", "coordinates"]
    assert data["geometry"]["type"] == "Point"
    assert type(data["geometry"]["coordinates"]) == list
    assert len(data["geometry"]["coordinates"]) == 2


def test_1314_watersheds(client):

    site_id = "AZR9-0903"
    response = client.get(f"/nrsa1314/watersheds/{site_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert list(data.keys()) == ["type", "geometry"]
    assert data["type"] == "Feature"
    assert list(data["geometry"].keys()) == ["type", "coordinates"]
    assert data["geometry"]["type"] == "Polygon"
    assert type(data["geometry"]["coordinates"]) == list
    assert len(data["geometry"]["coordinates"][0][0]) == 2
