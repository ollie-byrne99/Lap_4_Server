from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URL"]
db = SQLAlchemy(app)

app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"] 
jwt = JWTManager(app)
