from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import flask_bcrypt, db
from .user import User
from .pattern import Pattern
import stripe
import os

class Purchase(db.Model, SerializerMixin):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    pattern_id = db.Column(db.Integer, db.ForeignKey("patterns.id"), nullable=False)
    price = db.Column(db.Float)
    # stripe_product_id = db.Column(db.String)
    # stripe_price_id = db.Column(db.String)
    status = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationships
    user = db.relationship("User", back_populates="purchases")
    pattern = db.relationship("Pattern", back_populates="purchases")
    # pattern = db.relationship("Pattern", back_populates="purchases", primaryjoin='Pattern.id == Purchase.pattern_id')

    # Association Proxy


    # Serializer Rules
    serialize_rules = ("-user.purchases", "-pattern.purchases",)

    # Validations
    @validates("user_id")
    def validate_user_id(self, _, user_id):
        if not isinstance(user_id, int):
            raise TypeError("User id must be an integer")
        elif user_id < 1:
            raise ValueError(f"{user_id} has to be a positive integer")
        elif not db.session.get(User, user_id):
            raise ValueError(f"{user_id} has to correspond to an existing user")
        else:
            return user_id

    @validates("pattern_id")
    def validate_pattern_id(self, _, pattern_id):
        if not isinstance(pattern_id, int):
            raise TypeError("Pattern id must be an integer")
        elif pattern_id < 1:
            raise ValueError(f"{pattern_id} must be a positive integer")
        elif not db.session.get(Pattern, pattern_id):
            raise ValueError(f"{pattern_id} has to correspond to an existing pattern")
        else:
            return pattern_id
        
    # def __init__(self, *args, **kwargs):
    #     super(Purchase, self).__init__(*args, **kwargs)
    #     self. create_stripe_product_and_price()

    # def create_stripe_product_and_price(self):
    #     stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

    #     if not self.stripe_product_id or not self.stripe_price_id:
    #         stripe_product = stripe.Product.create(
    #             name =self.title,
    #             description=self.description,
    #             type="good",
    #         )

    #         stripe_price = stripe.Price.create(
    #             product=stripe_product.id,
    #             unit_amount=int(self.price * 100),
    #             currency="usd",
    #         )

    #         self.stripe_product_id = stripe_product.id
    #         self.stripe_price_id = stripe_price.id

    #         db.session.commit()
