from src.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Online Book Store"


def test_books():
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json) == 2