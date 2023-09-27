from flask import jsonify, request
from werkzeug import exceptions
from application import app
from application.recipes.controllers import index_recipe, create_recipe, show_recipe, update_recipe, destroy_recipe
from application.comments.controllers import index_comment, create_comment, show_comment, update_comment, destroy_comment
from application.users.controllers import register_user, show_user, update_user, destroy_user, index_user, login_user
from application.likes.controllers import index_like, create_like, show_like, update_like, destroy_like
from application.ingredients.controllers import index_ingredient, create_ingredient, show_ingredient, update_ingredient, destroy_ingredient

from flask_jwt_extended import jwt_required


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
        return jwt_required()(create_recipe)()
        
    if request.method == "GET":
        return index_recipe()

@app.route("/recipes/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_recipe(id):
    if request.method == "GET":
        return show_recipe(id)
    
    if request.method == "PATCH":
        return jwt_required()(update_recipe)(id)
    
    if request.method == "DELETE":
        return jwt_required()(destroy_recipe)(id)
    

@app.route("/comments", methods=["GET", "POST"])
def handle_comments():
    if request.method == "POST":
        return jwt_required()(create_comment)()
        
    if request.method == "GET":
        return index_comment()

@app.route("/comments/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_comment(id):
    if request.method == "GET":
        return show_comment(id)
    
    if request.method == "PATCH":
        
        return jwt_required()(update_comment)(id)
    
    if request.method == "DELETE":
        return jwt_required()(destroy_comment)(id)
    

@app.route("/register", methods=["POST"])
def handle_register():
    if request.method == "POST":
        return register_user()
    

@app.route("/login", methods=["POST"])
def handle_login():
    if request.method == "POST":
        return login_user()


@app.route("/users", methods=["GET"])
def handle_users():
    if request.method == "GET":
        return index_user()
        

@app.route("/users/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_user(id):
    if request.method == "GET":
        return show_user(id)
    
    if request.method == "PATCH":
        return update_user(id)
    
    if request.method == "DELETE":
        return destroy_user(id)
    


@app.route("/likes", methods=["GET", "POST"])
def handle_likes():
    if request.method == "POST":
        return jwt_required()(create_like)()
        
    if request.method == "GET":
        return index_like()

@app.route("/likes/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_like(id):
    if request.method == "GET":
        return show_like(id)
    
    if request.method == "PATCH":
        return jwt_required()(update_like)(id)
    
    if request.method == "DELETE":
        return jwt_required()(destroy_like)(id)
    

@app.route("/ingredients", methods=["GET", "POST"])
def handle_ingredients():
    if request.method == "POST":
        return jwt_required()(create_ingredient)()
        
    if request.method == "GET":
        return index_ingredient()

@app.route("/ingredients/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_ingredient(id):
    if request.method == "GET":
        return show_ingredient(id)
    
    if request.method == "PATCH":
        return jwt_required()(update_ingredient)(id)
    
    if request.method == "DELETE":
        return jwt_required()(destroy_ingredient)(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"Oops {err}"}), 400
