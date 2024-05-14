#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, g, session, send_file, abort, jsonify, redirect, render_template
from flask_restful import Resource
from functools import wraps
from werkzeug.security import generate_password_hash
from config import app, db, api
import os
import stripe
from datetime import datetime

from flask_migrate import Migrate
from flask_restful import Api
from sqlalchemy import MetaData
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_session import Session
from os import environ
import re
# Models
from models.user import User
from models.pattern import Pattern
from models.purchase import Purchase
from models.category import Category
from models.favorites import Favorite
# # Schemas
from schemas.user_schema import user_schema, users_schema
from schemas.pattern_schema import pattern_schema, patterns_schema
from schemas.purchase_schema import purchase_schema, purchases_schema
from schemas.category_schema import category_schema, categories_schema

from dotenv import load_dotenv

# load_dotenv()

# app = Flask(
#     __name__,
#     static_url_path='',
#     static_folder='../client/build',
#     template_folder='../client/build'
# )

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///cozyknots.db")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")
# app.config["SESSION_TYPE"] = "sqlalchemy"

# stripe_keys = {
#     "secret_key": os.environ.get("STRIPE_SECRET_KEY"),
#     "publishable_key": os.environ.get("STRIPE_PUBLISHABLE_KEY"),
# }

# db = SQLAlchemy(app)
# app.config["SESSION_SQLALCHEMY"] = db
# migrate = Migrate(app, db)
# api = Api(app)
# ma = Marshmallow(app)
# session = Session(app)
# flask_bcrypt = Bcrypt(app)

# Views go here!

# @app.route('/')
# def index(id=0):
#     return render_template('index.html')

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
    data = request.get_json()

    # Validate required fields
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Username, email, and password are required"}), 422

    # Validate email format
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.match(email_regex, data.get('email')):
        return jsonify({"error": "Invalid email format"}), 422

    # Validate password strength (example: at least 6 characters)
    if len(data.get('password')) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 422

    # Check if user already exists
    existing_user = User.query.filter_by(email=data.get('email')).first()
    if existing_user:
        return jsonify({"error": "User with this email already exists"}), 422

    # Create new user
    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        password_hash=generate_password_hash(data.get('password'))
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


# def signup():
#     try:
#         data = request.json
#         user = user_schema.load(data, partial=True)
#         db.session.add(user)
#         db.session.commit()
#         session["user_id"] = user.id
#         return user_schema.dump(user), 201
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 422
    
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data["username"]).first()
        if user and user.authenticate(data.get("password_hash")):
            session["user_id"] = user.id
            return user_schema.dump(user), 200
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

# #! ALL PATTERN RELATED ROUTES
class Patterns(Resource):
    # @login_required
    def get(self):
        try:
            serialized_pattern = patterns_schema.dump(Pattern.query)
            return serialized_pattern, 200
        except Exception as e:
            return {"error": str(e)}, 400
        
    def post(self):
        try:
            data = request.json
            # file = request.files['pattern_file']
            category_id = data.get('category_id') 
            category = Category.query.filter_by(id=category_id).first()
            if not category:
                return {'error': 'Category not found'}, 404
            
            is_free = data.get('is_free', False)

            if is_free:
                price=0
            else:
                price = data.get('price')
                print(price)
                if not price or price <= 0:
                    return {'error': 'Price must be greater than 0 for priced patterns'}, 422
            
            pattern = Pattern(
                title=data['title'],
                description=data['description'],
                price=float(price),
                author=data['author'],
                difficulty=data['difficulty'],
                type=data['type'],
                category=category,
                is_free=is_free,
                image=data['image']
            )
            # pattern.pattern_file = file.name
            db.session.add(pattern)
            db.session.commit()
            return pattern_schema.dump(pattern), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422
        
class PatternById(Resource):
    # @login_required
    def get(self, id):
        try:
            pattern = Pattern.query.get(id)
            if not pattern:
                abort(404, message="Pattern not found")
            return pattern_schema.dump(pattern), 200
        except Exception as e:
            return {"error": str(e)}, 400
        
    def post(self, id):
        user_id = request.json.get('user_id')
        pattern = Pattern.query.get(id)
        if not pattern:
            abort(404, message="Pattern not found")
        if pattern.is_free:
            return jsonify({"message": "Pattern downloaded successfully", "pattern": pattern_schema.dump(pattern)}), 200
        
        purchase = Purchase.query.filter_by(user_id=user_id, pattern_id=id).first()
        if purchase:
            return jsonify({"message": "Pattern downloaded successfully", "pattern": pattern_schema.dump(pattern)}), 200
        else:
            return jsonify({"message": "Purchase required to download the pattern"}), 402
        
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
            
# #! ALL USER RELATED ROUTES
class Users(Resource):
    @login_required
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
    @login_required
    # def get(self, id):
    #     try:
    #         if g.user:
    #             return user_schema.dump(g.user), 200
    #     except Exception as e:
    #         return {"error": str(e)}, 400
    
    @login_required
    def patch(self, id):
        try:
            user = db.session.get(User, session["user_id"])
            if user:
                data = request.json
                updated_user = user_schema.load(data, instance=user, partial=True)
                db.session.commit()
                return user_schema.dump(updated_user), 200
            else:
                return {"error": "User not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400
    
    @login_required        
    def delete(self, id):
        try:
            user = db.session.get(User, session["user_id"])
            if user:
                db.session.delete(user)
                db.session.commit()
                return {}, 204
        except Exception as e:
            return {"error": str(e)}, 400
        
#! FAVORITES
class Favorites(Resource):
    def get(self, user_id):
        try:
            favorited_patterns = Favorite.query.filter_by(user_id=user_id).all()
            serialized_patterns = [pattern.to_dict() for pattern in favorited_patterns]
            return jsonify({"favoritedPatterns": serialized_patterns}), 200
        except Exception as e:
            return {"error": str(e)}, 500
    
    def post(self, pattern_id):
        try:
            user_id = session["user_id"]
            favorite = Favorite(user_id=user_id, pattern_id=pattern_id)
            db.session.add(favorite)
            db.session.commit()
            return {"message": "Pattern added to favorite successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422
    
    def delete(self, pattern_id):
        try:
            user_id = session["user_id"]
            favorite = Favorite.query.filter_by(user_id=user_id, pattern_id=pattern_id).first()
            if favorite:
                db.session.delete(favorite)
                db.session.commit()
                return {"message": "Pattern removed from favorites successfully"}, 204
            else:
                return {"message": "Pattern is not in favorites"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422
        
@app.route("/favorites/<int:user_id>", methods=["GET"])
def get_favorited_patterns(user_id):
    try:
        favorited_patterns = Favorite.query.filter_by(user_id=user_id).all()
        serialized_patterns = [pattern.to_dict() for pattern in favorited_patterns]
        return jsonify({"favoritedPatterns": serialized_patterns}), 200
    except Exception as e:
        return {"error": str(e)}, 500
        
# #! ALL PURCHASE RELATED ROUTES
class Purchases(Resource):
    @login_required
    def get(self):
        try:
            if "user_id" not in session:
                return {"error": "User not logged in"}, 401
            user_id = session["user_id"]
            purchases = Purchase.query.filter_by(user_id=user_id).all()
            serialized_purchases = purchases_schema.dump(purchases)
            return serialized_purchases, 200
        except Exception as e:
            return {"error": str(e)}, 400
    
    def post():
        try:
            data = request.json
            user_id = data.get("user_id")
            pattern_id = data.get("pattern_id")
            price = data.get("price")
            status = data.get("status", "pending")  # Default status to "pending" if not provided

            # Create a new Purchase record
            purchase = Purchase(user_id=user_id, pattern_id=pattern_id, price=price, status=status)
            db.session.add(purchase)
            db.session.commit()

            return {"message": "Purchase successfully created"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422

class PurchaseById(Resource):
    def get(self, id):
        try:
            # import ipdb; ipdb.set_trace()
            user = User.query.get(session["user_id"])
            purchase = Purchase.query.filter_by(id=id).first()
            if purchase:
                purchase.status = "Completed"
                purchase.purchase_date = datetime.now()
                # return redirect("http://localhost:3000/success"), 200
                return purchases_schema.dump(user.purchases), 200
            else:
                return {"error": f"Purchase {id} not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400
        
class Categories(Resource):
    def get(self):
        try:
            serialized_category = categories_schema.dump(Category.query)
            return serialized_category, 200
        except Exception as e:
            return {"error": str(e)}, 400

YOUR_DOMAIN = "http://localhost:3000"
stripe_secret_key = os.environ.get("STRIPE_SECRET_KEY")
if not stripe_secret_key:
    raise ValueError("STRIPE_SECRET_KEY is not set in the environment variables.")
stripe.api_key = stripe_secret_key

@app.route('/create-checkout-session/<int:id>', methods=['POST'])
def create_checkout_session(id):
    try:
        pattern_to_purchase = db.session.get(Pattern, id)
        if pattern_to_purchase:
            new_purchase_data = {
                "user_id": session.get("user_id"),
                "pattern_id": pattern_to_purchase.id,
                "price": pattern_to_purchase.price,
                "status": "Pending",
            }
            new_purchase = Purchase(**new_purchase_data)

            db.session.add(new_purchase)
            db.session.commit()
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': pattern_to_purchase.stripe_price_id,
                        'quantity': 1
                    }
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + f"/success/{new_purchase.id}",
                cancel_url=YOUR_DOMAIN + "/cancelled"
            )
            return redirect(checkout_session.url, code=303)
        else:
            return {"message": "Pattern not found"}, 404
        import ipdb; ipdb.set_trace()
    except Exception as e:
        return {"message": str(e)}

#BACKEND ROUTES
api.add_resource(Categories, "/categories")
api.add_resource(Patterns, "/patterns")
api.add_resource(PatternById, "/patterns/<int:id>")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Purchases, "/purchases")
api.add_resource(PurchaseById, "/success/<int:id>")
api.add_resource(Favorites, "/favorites/<int:pattern_id>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5555)))
#FRONTEND
@app.route("/registration")
@app.route("/user/:<int:id>")
@app.route("/")
@app.route("/cart")
@app.route("/success/:<int:id>")
@app.route("/community")

def index(id=0):
    return render_template("index.html")
