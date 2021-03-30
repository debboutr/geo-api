import json


def test_0809_points(client):

    response = client.get("/nrsa0809/points/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert list(data.keys()) == ["type", "features"]
    assert data["type"] == "FeatureCollection"
    assert type(data["features"]) == list
    assert len(data["features"]) == 2105
    feature = data["features"][0]
    assert list(feature.keys()) == ["type", "properties", "geometry"]
    assert feature["type"] == "Feature"
    assert list(feature["properties"].keys()) == [
        "SITE_ID",
        "DATE_COL",
        "YEAR",
        "VISIT_NO",
    ]


def test_0809_site_detail(client):

    site_id = "FW08AZ019"
    response = client.get(f"/nrsa0809/point/{site_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert list(data.keys()) == ["type", "geometry", "properties"]
    assert data["type"] == "Feature"
    assert list(data["geometry"].keys()) == ["type", "coordinates"]
    assert data["geometry"]["type"] == "Point"
    assert type(data["geometry"]["coordinates"]) == list
    assert len(data["geometry"]["coordinates"]) == 2


def test_0809_watersheds(client):

    site_id = "FW08AZ019"
    response = client.get(f"/nrsa0809/watersheds/{site_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert list(data.keys()) == ["type", "geometry"]
    assert data["type"] == "Feature"
    assert list(data["geometry"].keys()) == ["type", "coordinates"]
    assert data["geometry"]["type"] == "Polygon"
    assert type(data["geometry"]["coordinates"]) == list
    assert len(data["geometry"]["coordinates"][0][0]) == 2
