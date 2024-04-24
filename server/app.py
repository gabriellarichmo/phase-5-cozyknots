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

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.before_request
def before_request():
    pass

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        pass

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

