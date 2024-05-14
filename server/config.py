from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from sqlalchemy import MetaData
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_session import Session
from os import environ
import os
import stripe
from dotenv import load_dotenv

# Instantiate app, set attributes
app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cozyknots.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
app.secret_key = environ.get("SESSION_SECRET")
app.config["SESSION_TYPE"] = "sqlalchemy"

# app.config["STRIPE_PUBLISHABLE_KEY"]=os.environ.get("STRIPE_PUBLISHABLE_KEY")
# app.config["STRIPE_SECRET_KEY"]=os.environ.get("STRIPE_SECRET_KEY")
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URL"] = os.environ.get("DATABASE_URL")

stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
}

stripe.api_key = stripe_keys["secret_key"]


db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

migrate = Migrate(app, db)
api = Api(app)
ma = Marshmallow(app)
session = Session(app)
flask_bcrypt = Bcrypt(app)
