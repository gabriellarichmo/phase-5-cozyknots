from config import ma, db
import re
from models.user import User
from marshmallow import validate, validates, ValidationError, fields, validate, validates_schema

class UserSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = User
        load_instance = True
        exclude=("_password_hash",)
        
    patterns = fields.Nested(
        "PatternSchema",
        only=("id",),
        # exclude=("user",),
    )
    
    purchases = fields.Nested(
        "PurchaseSchema",
        many=True,
        exclude=("user",),  # Exclude the user field to avoid circular reference
        only=("id",),
        # only=("id", "adopt", "foster", "created_at", "updated_at", "cat_id"),  # Include cat_id
    )
    
    username = fields.String(required=True, validate=validate.Length(min=2,max=20))
    email = fields.String(required=True, validate=[validate.Email()])
    password_hash = fields.String(data_key="password_hash", required=True, validate=validate.Length(min=5), load_only=True)
    # interest = fields.String(required=False)
    
    # @validates_schema
    # def validate_email(self, data, **kwargs):
    #     email = data.get("email")
        
    #     if User.query.filter_by(email=email).first():
    #         raise ValidationError(f"Email {email} already exists.") #! EXTRACT ONLY THE STRING
    
    def load(self, data, instance=None, *, partial=False, **kwargs):
        loaded_instance = super().load(
            data, instance=instance, partial=partial, **kwargs
        )
        
        for key, value in data.items():
            setattr(loaded_instance, key, value)
        return loaded_instance

user_schema = UserSchema()
users_schema = UserSchema(many=True)