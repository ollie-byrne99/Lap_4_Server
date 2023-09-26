from flask import jsonify, request
from werkzeug import exceptions
from application import app
from application.recipes.controllers import index_recipe, create_recipe, show_recipe, update_recipe, destroy_recipe
from application.comments.controllers import index_comment, create_comment, show_comment, update_comment, destroy_comment
from application.users.controllers import register_user, show_user, update_user, destroy_user

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
        return create_recipe()
        
    if request.method == "GET":
        return index_recipe()

@app.route("/recipes/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_recipe(id):
    if request.method == "GET":
        return show_recipe(id)
    
    if request.method == "PATCH":
        return update_recipe(id)
    
    if request.method == "DELETE":
        return destroy_recipe(id)
    

@app.route("/comments", methods=["GET", "POST"])
def handle_comments():
    if request.method == "POST":
        return create_comment()
        
    if request.method == "GET":
        return index_comment()

@app.route("/comments/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_comment(id):
    if request.method == "GET":
        return show_comment(id)
    
    if request.method == "PATCH":
        return update_comment(id)
    
    if request.method == "DELETE":
        return destroy_comment(id)
    

@app.route("/register", methods=["POST"])
def handle_register():
    if request.method == "POST":
        return register_user()
        

@app.route("/users/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_user(id):
    if request.method == "GET":
        return show_user(id)
    
    if request.method == "PATCH":
        return update_user(id)
    
    if request.method == "DELETE":
        return destroy_user(id)
    

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"Oops {err}"}), 400
