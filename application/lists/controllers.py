from .models import List
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index_list():
    try:
        lists = List.query.all()
        data = [l.json for l in lists]
        return jsonify({"lists": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    

def create_list():
    try:
        data = request.json
        attributes = [
            "user_id", "items"
        ]

        extracted_data = {attr: data.get(attr) for attr in attributes}

        new_list = List(**extracted_data)

        db.session.add(new_list)
        db.session.commit()

        return jsonify({"data": new_list.json}), 201

    except:
        raise exceptions.InternalServerError("We cannot process your request.")
    
def show_list(id):
    try:
        list = List.query.filter_by(id=id).first()
        return jsonify({"data": list.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")
    

def update_list(id):
    data = request.json
    list = List.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(list, attribute):
            setattr(list, attribute, value)

    db.session.commit()

    return jsonify({ "data": list.json })

def destroy_list(id):
    list = List.query.filter_by(id=id).first()
    db.session.delete(list)
    db.session.commit()
    return f"List Deleted", 204
