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


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)