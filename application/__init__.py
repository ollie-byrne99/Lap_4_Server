from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from . import router
import os

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URL"]

db = SQLAlchemy(app)
