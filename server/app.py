#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, g, session, send_file
from flask_restful import Resource
from functools import wraps
from werkzeug.security import generate_password_hash
from config import app, db, api
import os
# Models
from models.user import User
from models.pattern import Pattern
from models.purchase import Purchase
from models.category import Category
# # Schemas
from schemas.user_schema import user_schema, users_schema
from schemas.pattern_schema import pattern_schema, patterns_schema
from schemas.purchase_schema import purchase_schema, purchases_schema
from schemas.category_schema import category_schema, categories_schema

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

# #! ALL REGISTRATION RELATED ROUTES
@app.route("/signup", methods=["POST"])
def signup():
    # try:
    #     data = request.json
    #     username = data.get("username")
    #     email = data.get("email")
    #     password = data.get("password")
    #     user = User(username=username, email=email)
    #     user.password_hash = password
    #     db.session.add(user)
    #     db.session.commit()
    #     session["user_id"] = user.id
    #     return user.to_dict(), 201
    # except Exception as e:
    #     db.session.rollback()
    #     return {"message": str(e)}, 422
    try:
        data = request.json
        user = user_schema.load(data, partial=True)
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id
        return user_schema.dump(user), 201
    except Exception as e:
        db.session.rollback()
        # logging.error(f"Error during signup: {e}")
        return {"error": str(e)}, 422
    
@app.route("/login", methods=["POST"])
def login():
    # try:
    #     data = request.json 
    #     user = User.query.filter_by(email=data.get("email")).first()
    #     if user and user.authenticate(data.get("password")):
    #         session["user_id"] = user.id
    #         return user.to_dict(), 200
    #     else:
    #         return {"message": "Invalid Credentials"}, 422
    # except Exception as e:
    #     return {"message": str(e)}, 422
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
    
@app.route("/current_user", methods=["GET"])
def current_user():
    try:
        if "user_id" in session:
            user = db.session.get(User, session.get("user_id"))
            return user_schema.dump(user), 200
        else:
            return {"message": "Please log in"}, 400
    except Exception as e:
        return {"error": str(e)}
    # try:
    #     if "user_id" in session:
    #         user = db.session.get(User, session.get("user_id"))
    #         return user_schema.dump(user), 200
    #     else:
    #         return {"message": "Please log in!"}, 400
    # except Exception as e:
    #     return {"error": str(e)}, 500

# #! ALL PATTERN RELATED ROUTES
class Patterns(Resource):
    def get(self):
        try:
            serialized_pattern = patterns_schema.dump(Pattern.query)
            return serialized_pattern, 200
        except Exception as e:
            return {"error": str(e)}, 400
        
    def post(self):
        try:
            data = request.json
            category_id = data.get('category_id')
            category = Category.query.get(category_id)
            if not category:
                return {'error': 'Category not found'}, 404
            pattern = Pattern(
                title=data['title'],
                description=data['description'],
                price=data['price'],
                author=data['author'],
                difficulty=data['difficulty'],
                category=category
            )
            db.session.add(pattern)
            db.session.commit()
            return pattern_schema.dump(pattern), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422
        
class PatternById(Resource):
    def get(self, id):
        try:
            return pattern_schema.dump(g.pattern), 200
        except Exception as e:
            return {"error": str(e)}, 400
        
    def patch(self, id):
        if g.pattern:
            try:
                data = request.json
                updated_pattern = pattern_schema.load(data, instance=g.pattern, partial=True)
                db.session.commit()
                return pattern_schema.dump(updated_pattern), 200
            except Exception as e:
                return {"error": str(e)}, 400
        else:
            return {"error": f"Pattern {id} not found"}, 404
    
@app.route('/images/<path:image_path>')
def get_image(image_path):
    image_folder = 'pattern_pictures'
    full_path = os.path.join(image_folder, image_path)
    print(full_path)
    return send_file(full_path, mimetype='image/jpeg') 
            
    #! could be problematic - hide pattern from profile instead of deleting from all users that purchased/downloaded
    # def delete(self, id):
    #     if g.pattern:
    #         try:
    #             db.session.delete(g.pattern)
    #             db.session.commit()
    #             return {}, 204
    #         except Exception as e:
    #             db.session.rollback()
    #             return {"error": str(e)}, 400
    #     else:
    #         return {"error": f"Unable to delete pattern {id} at this time."}, 404

# #! ALL USER RELATED ROUTES
class Users(Resource):
    def get(self):
        try:
            serialized_user = users_schema.dump(User.query)
            return serialized_user, 200
        except Exception as e:
            return {"error": str(e)}, 400
        
    def post(self):
        try:
            data = (request.json)
            user = user_schema.load(data)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422

class UserById(Resource):
    def get(self, id):
        try:
            if g.user:
                return user_schema.dump(g.user), 200
        except Exception as e:
            return {"error": str(e)}, 400
    
    def patch(self, id):
        try:
            if g.user:
                data = request.json
                updated_user = user_schema.load(data, instance=g.user, partial=True)
                db.session.commit()
                return user_schema.dump(updated_user), 200
        except Exception as e:
            return {"error": str(e)}, 400
            
    def delete(self, id):
        try:
            if g.user:
                db.session.delete(g.user)
                db.session.commit()
                return {}, 204
        except Exception as e:
            return {"error": str(e)}, 400
        
# #! ALL PURCHASE RELATED ROUTES
class Purchases(Resource):
    def get(self, id):
        try:
            serialized_purchases = purchases_schema.dump(Purchase.query)
            return serialized_purchases, 200
        except Exception as e:
            return {"error": str(e)}, 400
    
    #! not needed?
    # def patch(self, id):
    #     try:
    #         pass
    #     except Exception as e:
    #         return {"error": str(e)}, 400
            
    #! not needed?
    # def delete(self, id):
    #     try:
    #         pass
    #     except Exception as e:
    #         return {"error": str(e)}, 400

class PurchaseById(Resource):
    def get(self, id):
        try:
            purchase = Purchase.query.filter_by(pattern_id=id).first()
            if purchase:
                confirm_purchase = purchase.pattern.title
                return {"message": f"You have purchased {confirm_purchase}"}, 200
            else:
                return {"error": f"Purchase {id} not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400
        
class Categories(Resource):
    def get(self):
        categories = [category.to_dict() for category in Category.query]
        return categories, 200


api.add_resource(Categories, "/categories")
api.add_resource(Patterns, "/patterns")
api.add_resource(PatternById, "/patterns/<int:id>")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Purchases, "/purchases")
api.add_resource(PurchaseById, "/purchases/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)

