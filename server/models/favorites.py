from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import flask_bcrypt, db
from sqlalchemy.orm import relationship

class Favorite(db.Model):
  __tablename__ = 'favorites'

  id = db.Column(db.Integer, primary_key=True)
  pattern_id = db.Column(db.Integer, db.ForeignKey('patterns.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  pattern = db.relationship('Pattern', back_populates='favorites')
  user = db.relationship('User', back_populates='favorites')