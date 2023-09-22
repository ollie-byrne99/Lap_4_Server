from flask import jsonify, request
from application import app

@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Recipe API",
        "endpoints": [
            "GET /"
        ]
    }), 200
