from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qsvzyace:gqPw0yrmK9WaDzeC9EJaBCy5K1z2_-GV@tai.db.elephantsql.com/qsvzyace'


db = SQLAlchemy(app)
