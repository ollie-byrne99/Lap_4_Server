from .models import Like
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index_like():
    try:
        likes = Like.query.all()
        data = [l.json for l in likes]
        return jsonify({"likes": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    

def create_like():
    try:
        data = request.json
        attributes = [
            "user_id", "recipe_id"
        ]

        extracted_data = {attr: data.get(attr) for attr in attributes}

        new_like = Like(**extracted_data)

        db.session.add(new_like)
        db.session.commit()

        return jsonify({"data": new_like.json}), 201

    except:
        raise exceptions.InternalServerError("We cannot process your request.")
    
def show_like(id):
    try:
        like = Like.query.filter_by(id=id).first()
        return jsonify({"data": like.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")
    

def update_like(id):
    data = request.json
    like = Like.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(like, attribute):
            setattr(like, attribute, value)

    db.session.commit()

    return jsonify({ "data": like.json })

def destroy_like(id):
    like = Like.query.filter_by(id=id).first()
    db.session.delete(like)
    db.session.commit()
    return f"Like Deleted", 204
