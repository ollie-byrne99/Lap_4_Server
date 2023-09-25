from .models import User
# from .models import Token
from werkzeug import exceptions
from flask import jsonify
from flask import jsonify, request
from .. import db



def show_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        return jsonify({"data": user.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")
    

def create_user():
    try:
        data = request.json
        attributes = [
            "username","password"
        ]

        extracted_data = {attr: data.get(attr) for attr in attributes}

        new_user = User(**extracted_data)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"data": new_user.json}), 201

    except:
        raise exceptions.InternalServerError("We cannot process your request.")
