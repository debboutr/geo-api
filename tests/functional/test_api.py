import json


def test_home_page(client):

    response = client.get("/")
    assert response.status_code == 200
    assert (
        b"GeoAPI for National Aquatic Resource Surveys"
        in response.data
    )


def test_swagger_json(client):

    response = client.get("/swagger.json")
    assert response.status_code == 200


