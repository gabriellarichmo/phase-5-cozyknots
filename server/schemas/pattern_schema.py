from config import ma
from marshmallow import validate, validates, ValidationError, fields, validate
from models.pattern import Pattern

class PatternSchema(ma.SQLAlchemyAutoSchema):
    category = fields.Nested('CategorySchema', exclude=('patterns',))
    pattern_file = fields.String()
    class Meta:
        model = Pattern
        load_instance = True
    
    is_free = fields.Boolean(required=True)
    download_link = fields.String()

    title = fields.String(required=True, validate=validate.Length(min=2, max=50, error="Title must be between 2 and 50 characters."))
    description = fields.String(required=True, validate=validate.Length(min=2, max=250, error="Description must be between 1 and 250 characters."))
    price = fields.Float(required=True, validate=validate.Range(min=1, max=10, error="Price must be between 1 and 10."))
    difficulty = fields.String(required=True, validate=validate.OneOf(["Beginner", "Intermediate", "Advanced"], error="Difficulty must be one of: Beginner, Intermediate, Advanced."))
    category_id = fields.Integer(required=True)
    image = fields.String()

pattern_schema = PatternSchema()
patterns_schema = PatternSchema(many=True)