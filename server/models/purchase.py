from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import flask_bcrypt, db
from .user import User

class Purchase(db.Model, SerializerMixin):
  __tablename___ = "purchases"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  pattern_id = db.Column(db.Integer, db.ForeignKey("patterns.id"))
  price = db.Column(db.Float)
  payment_method = db.Column(db.String)
  status = db.Column(db.String)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, onupdate=db.func.now())

  # Relationships
  user = db.relationship("User", back_populates="purchases")
  pattern = db.relationship("Pattern", back_populates="purchases")

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
          raise ValueError(f"{user_id} has to correspond to an existing production")
      return user_id