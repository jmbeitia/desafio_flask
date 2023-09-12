from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_migrate import Migrate


load_dotenv()

app = Flask(__name__)
prodURI = os.environ['DATABASE_URI']

app.config['SQLALCHEMY_DATABASE_URI'] = prodURI
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)
