from config import ma
from marshmallow import fields, validate
from models.category import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
  patterns = fields.Nested(
    "PatternSchema",
    many=True, 
    xclude=('category',)
  )

  class Meta:
    model = Category
    load_instance = True


  name = fields.String(required=True, validate=validate.OneOf(["Sweaters", "Amigurumi", "Mittens", "Scarves", "Socks", "Hats", "Other"], error="Category name must be any of: Sweaters, Amigurumi, Mittens, Scarves, Socks, Hats, or Other."))


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)