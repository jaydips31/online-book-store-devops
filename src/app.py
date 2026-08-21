from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Online Book Store",
        "status": "running"
    })


@app.route("/books")
def books():
    return jsonify([
        {
            "id": 1,
            "title": "Python Basics",
            "author": "John Doe"
        },
        {
            "id": 2,
            "title": "DevOps Fundamentals",
            "author": "Jane Doe"
        }
    ])


@app.route("/books/1")
def book_one():
    return jsonify({
        "id": 1,
        "title": "Python Basics",
        "author": "John Doe"
    })


@app.route("/users")
def users():
    return jsonify([
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
    ])


@app.route("/users/1")
def user_one():
    return jsonify({
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    })


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if email == "john@example.com" and password == "password123":
        return jsonify({
            "message": "Login successful",
            "user_id": 1
        })

    return jsonify({
        "message": "Invalid email or password"
    }), 401


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)