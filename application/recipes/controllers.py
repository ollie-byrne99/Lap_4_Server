from .models import Recipe
from werkzeug import exceptions
from flask import jsonify
from flask import jsonify, request
from .. import db

def index_recipe():
    try:
        recipes = Recipe.query.all()
        data = [r.json for r in recipes]
        return jsonify({"recipes": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    

def create_recipe():
    try:
        data = request.json
        attributes = [
            "name","description", "user_id"
        ]

        extracted_data = {attr: data.get(attr) for attr in attributes}

        new_recipe = Recipe(**extracted_data)

        db.session.add(new_recipe)
        db.session.commit()

        return jsonify({"data": new_recipe.json}), 201

    except:
        raise exceptions.InternalServerError("We cannot process your request.")
    
def show_recipe(id):
    try:
        recipe = Recipe.query.filter_by(id=id).first()
        return jsonify({"data": recipe.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")
    

def update_recipe(id):
    data = request.json
    recipe = Recipe.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(recipe, attribute):
            setattr(recipe, attribute, value)

    db.session.commit()

    return jsonify({ "data": recipe.json })


def destroy_recipe(id):
    recipe = Recipe.query.filter_by(id=id).first()
    db.session.delete(recipe)
    db.session.commit()
    return f"Recipe Deleted", 204
