from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import flask_bcrypt, db
import stripe
import os

class Pattern(db.Model, SerializerMixin):
  __tablename__ = "patterns"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(250), nullable=False)
  price = db.Column(db.Float)
  is_free = db.Column(db.Boolean)
  author = db.Column(db.String)
  difficulty = db.Column(db.String)
  type = db.Column(db.String)
  image = db.Column(db.String)
  stripe_product_id = db.Column(db.String)
  stripe_price_id = db.Column(db.String)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, onupdate=db.func.now())
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
  # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


  def __repr__(self):
    return f"""<Pattern {self.id}: 
                        Title: {self.title}, 
                        Author: {self.author}, 
                        Type: {self.type},
                        Description: {self.description}, 
                        Difficulty: {self.difficulty}, 
                        Price: {self.price} 
                        />
                        """

  # Relationships
  # purchases = db.relationship('Purchase', back_populates='pattern', primaryjoin='Pattern.id == Purchase.pattern_id')
  purchases = db.relationship('Purchase', back_populates='pattern')
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
  
  @validates("type")
  def validate_type(self, _, type):
    if not isinstance(type, str):
      raise TypeError("Type must be of type string.")
    elif type not in ["Knit", "Crochet"]:
      raise ValueError("Type must be either Knit or Crochet.")
    else:
      return type

  def __init__(self, *args, **kwargs):
      super(Pattern, self).__init__(*args, **kwargs)
      self. create_stripe_product_and_price()

  def create_stripe_product_and_price(self):
      stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

      if not self.stripe_product_id or not self.stripe_price_id:
          stripe_product = stripe.Product.create(
              name =self.title,
              description=self.description,
              type="good",
          )

          stripe_price = stripe.Price.create(
              product=stripe_product.id,
              unit_amount=int(self.price * 100),
              currency="usd",
          )

          self.stripe_product_id = stripe_product.id
          self.stripe_price_id = stripe_price.id

          db.session.commit()