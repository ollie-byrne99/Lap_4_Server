from .models import Token
from werkzeug import exceptions
from flask import jsonify
from flask import jsonify, request
from .. import db

def index_token():
    try:
        tokens = Token.query.all()
        data = [t.json for t in tokens]
        return jsonify({"tokens": data}), 200
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    
