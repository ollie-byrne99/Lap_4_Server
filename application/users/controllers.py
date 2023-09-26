from flask import request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from werkzeug import exceptions

from .models import User
from .. import db
from application import app

bcrypt = Bcrypt(app)

def register_user():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User Already Exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') 
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "password": new_user.password 
    })

def login_user():
    username = request.json["username"]
    password = request.json["password"]

    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"error": "Unauthorised"}), 401

    hashed_password = user.password

    if not bcrypt.check_password_hash(hashed_password, password):
        return jsonify({"error": "Unauthorised"}), 401

    access_token = create_access_token(identity={"username": username, "email": user.email})

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "token": access_token
    })

def index_user():
    try:
        users = User.query.all()
        data = [u.json for u in users]
        return jsonify({"users": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    
def show_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        return jsonify({"data": user.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")

def update_user(id):
    data = request.json
    user = User.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(user, attribute):
            setattr(user, attribute, value)

    db.session.commit()

    return jsonify({"data": user.json})

def destroy_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return f"User Deleted", 204
