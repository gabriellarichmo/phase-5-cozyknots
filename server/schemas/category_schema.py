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

  # knit = Category(name="Knit")
  # crochet = Category(name="Crochet")

  # db.session.add_all([knit, crochet])
  # db.session.commit()

  # knit_patterns = Category(name="Knit Patterns", parent=knit)
  # crochet_patterns = Category(name="Crochet Patterns", parent=crochet)

  # db.session.add_all([knit_patterns, crochet_patterns])
  # db.session.commit()

  # knit_category = Category.query.filter_by(name="Knit").first()
  # knit_subcategories = knit_category.children

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)