#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, g, session
from flask_restful import Resource
from functools import wraps
# Local imports
from config import app, db, api
# Models
from models.user import User
from models.pattern import Pattern
from models.purchase import Purchase
from models.category import Category
# Schemas
from schemas.user_schema import user_schema, users_schema
# from schemas.pattern_schema import pattern_schema, patterns_schema
# from schemas.purchase_schema import purchase_schema, purchases_schema
# from schemas.category_schema import category_schema, categories_schema

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.before_request
def before_request():
    path_dict = {"userbyid": User, "patternbyid": Pattern, "purchasebyid": Purchase}
    if request.endpoint in path_dict:

        id = request.view_args.get("id")
        record = db.session.get(path_dict.get(request.endpoint), id)
        key_name = "user" if request.endpoint == "userbyid" else "pattern"
        if request.endpoint == 'purchasebyid':
            key_name = "purchase"
        setattr(g, key_name, record)
        

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return {"message": "You must be logged in!"}, 422
        return func(*args, **kwargs)
    return decorated_function

#! ALL REGISTRATION RELATED ROUTES
@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        user = user_schema.load(data, partial=True)
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id
        return user_schema.dump(user), 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 422
    
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data["username"]).first()
        if user and user.authenticate(data.get("password_hash")):
            session["user_id"] = user.id
            return user.to_dict(), 200
        else:
            return {"message": "Invalid credentials"}, 422
    except Exception as e:
        return {"error": str(e)}, 422
    
@app.route("/logout", methods=["DELETE"])
def logout():
    try:
        if "user_id" in session:
            del session["user_id"]
        return {}, 204
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 422
    
@app.route("/check_session", methods=["GET"])
def check_session():
    try:
        if "user_id" in session:
            user = db.session.get(User, session.get("user_id"))
            return user.to_dict(), 200
        else:
            return {"message": "Please log in!"}, 400
    except Exception as e:
        return {"error": str(e)}, 422

#! ALL PATTERN RELATED ROUTES
class Patterns(Resource):
    def get(self):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
        
class PatternById(Resource):
    def get(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
        
    def post(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
        
    def delete(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400

#! ALL USER RELATED ROUTES
class UserById(Resource):
    def get(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
    
    def patch(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
            
    def delete(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
        
#! ALL PURCHASE RELATED ROUTES
class Purchases(Resource):
    def get(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
    
    def patch(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400
            
    def delete(self, id):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}, 400



api.add_resource(Patterns, "/patterns")
api.add_resource(PatternById, "/patterns/<int:id>")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Purchases, "/purchases/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)

