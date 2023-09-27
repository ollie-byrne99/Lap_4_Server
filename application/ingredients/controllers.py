from .models import Ingredient
from werkzeug import exceptions
from flask import jsonify, request
from .. import db

def index_ingredient():
    try:
        ingredients = Ingredient.query.all()
        data = [i.json for i in ingredients]
        return jsonify({"ingredients": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    

def create_ingredient():
    try:
        data = request.json
        attributes = [
            "name","description", "season", "image"
        ]

        extracted_data = {attr: data.get(attr) for attr in attributes}

        new_ingredient = Ingredient(**extracted_data)

        db.session.add(new_ingredient)
        db.session.commit()

        return jsonify({"data": new_ingredient.json}), 201

    except:
        raise exceptions.InternalServerError("We cannot process your request.")
    
def show_ingredient(id):
    try:
        ingredient = Ingredient.query.filter_by(id=id).first()
        return jsonify({"data": ingredient.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")


def update_ingredient(id):
    data = request.json
    ingredient = Ingredient.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(ingredient, attribute):
            setattr(ingredient, attribute, value)

    db.session.commit()

    return jsonify({ "data": ingredient.json })


def destroy_ingredient(id):
    ingredient = Ingredient.query.filter_by(id=id).first()
    db.session.delete(ingredient)
    db.session.commit()
    return f"Ingredient Deleted", 204
