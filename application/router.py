from flask import jsonify, request
from werkzeug import exceptions
from application import app
from application.recipes.controllers import index, create, show, update, destroy
from application.comments.controllers import index_c, create_c, show_c, update_c, destroy_c

@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Recipe API",
        "endpoints": [
            "GET /"
        ]
    }), 200

@app.route("/recipes", methods=["GET", "POST"])
def handle_recipes():
    if request.method == "POST":
        return create()
        
    if request.method == "GET":
        return index()

@app.route("/recipes/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_recipe(id):
    if request.method == "GET":
        return show(id)
    
    if request.method == "PATCH":
        return update(id)
    
    if request.method == "DELETE":
        return destroy(id)
    

@app.route("/comments", methods=["GET", "POST"])
def handle_comments():
    if request.method == "POST":
        return create_c()
        
    if request.method == "GET":
        return index_c()

@app.route("/comments/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_comment(id):
    if request.method == "GET":
        return show_c(id)
    
    if request.method == "PATCH":
        return update_c(id)
    
    if request.method == "DELETE":
        return destroy_c(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"Oops {err}"}), 400
