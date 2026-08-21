from flask import Flask, jsonify
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


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)