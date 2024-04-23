from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import flask_bcrypt, db

class Category(db.Model, SerializerMixin):
  __tablename___ = "categories"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  description = db.Column(db.String, nullable=False)
  parent_category = db.Column(db.String)
  pattern_id = db.Column(db.Integer, db.ForeignKey('patterns.id'))

  # Relationships
  patterns = db.relationship('Pattern', back_populates='category')

  # Association Proxy

  
  # Serializer Rules
  
  
  # Validations