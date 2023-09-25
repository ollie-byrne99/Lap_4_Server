from .models import Comment
from werkzeug import exceptions
from flask import jsonify
from flask import jsonify, request
from .. import db

def index_c():
    try:
        comments = Comment.query.all()
        data = [c.json for c in comments]
        return jsonify({"comments": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    

def create_c():
    try:
        data = request.json
        attributes = [
            "comment", "recipe_id"
        ]

        extracted_data = {attr: data.get(attr) for attr in attributes}

        new_comment = Comment(**extracted_data)

        db.session.add(new_comment)
        db.session.commit()

        return jsonify({"data": new_comment.json}), 201

    except:
        raise exceptions.InternalServerError("We cannot process your request.")
    
def show_c(id):
    try:
        comment = Comment.query.filter_by(id=id).first()
        return jsonify({"data": comment.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")
    

def update_c(id):
    data = request.json
    comment = Comment.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(comment, attribute):
            setattr(comment, attribute, value)

    db.session.commit()

    return jsonify({ "data": comment.json })


def destroy_c(id):
    comment = Comment.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return f"Comment Deleted", 204