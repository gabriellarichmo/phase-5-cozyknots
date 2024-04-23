from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import flask_bcrypt, db

class Pattern(db.Model, SerializerMixin):
  __tablename___ = "patterns"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(250), nullable=False)
  price = db.Column(db.Float)
  author = db.Column(db.String)
  difficulty = db.Column(db.String)
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, onupdate=db.func.now())

  def __repr__(self):
    return f"""<Pattern {self.id}: 
                        Title: {self.title}, 
                        Author: {self.author}, 
                        Description: {self.description}, 
                        Difficulty: {self.difficulty}, 
                        Price: {self.price} 
                        />
                        """

  # Relationships
  purchases = db.relationship('Purchase', back_populates='patterns')
  category = db.relationship('Category', back_populates='patterns')
  
  # Association Proxy
  users = association_proxy("purchases", "user")
  
  #! Serializer Rules - Possibly not needed here.
  # serialize_rules = ("-purchases.pattern",)

  # Validations
  @validates("title")
  def validate_title(self, _, title):
    if not isinstance(title, str):
      raise TypeError("Title must be a string.")
    elif 2 > len(title) > 50:
      raise ValueError("Title must be at least 2 characters long and no longer than 50 characters.")
    else:
      return title
  
  @validates("price")
  def validate_price(self, _, price):
    if not isinstance(price, float):
      raise TypeError("Price must be a float")
    elif price > 10:
      raise ValueError("Price cannot be more than 10 dollars.")
    else:
      return price
  
  @validates("difficulty")
  def validate_difficulty(self, _, difficulty):
    if not isinstance(difficulty, str):
      raise TypeError("Difficulty must be of type string.")
    elif difficulty not in ["Beginner", "Intermediate", "Advanced"]:
      raise ValueError("Difficulty must be either Beginner, Intermediate, or Advanced.")
    else:
      return difficulty