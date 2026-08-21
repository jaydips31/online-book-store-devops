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


def test_book_one():
    client = app.test_client()

    response = client.get("/books/1")

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["title"] == "Python Basics"


def test_users():
    client = app.test_client()

    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json) == 2


def test_user_one():
    client = app.test_client()

    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["name"] == "John Doe"


def test_login_success():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "email": "john@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert response.json["message"] == "Login successful"
    assert response.json["user_id"] == 1


def test_login_invalid_password():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "email": "john@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401
    assert response.json["message"] == "Invalid email or password"