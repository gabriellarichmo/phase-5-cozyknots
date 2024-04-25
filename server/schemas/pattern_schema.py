# from config import ma
# from marshmallow import validate, validates, ValidationError, fields, validate
# from models.pattern import Pattern

# class PatternSchema(ma.SQLAlchemyAutoSchema):
    
#     class Meta:
#         model = Pattern
#         load_instance = True
#         # exclude = ["created_at", "updated_at"]
        

#     price = fields.Float(required=True, validate=validate.Length(min=1,max=10, error=""))
#     difficulty = fields.String(required=True, validate=validate.Length(min=2,max=15, error=""))

# pattern_schema = PatternSchema()
# patterns_schema = PatternSchema(many=True)