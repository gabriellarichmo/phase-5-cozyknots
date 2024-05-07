from config import ma, db
import re
from models.user import User
from marshmallow import validate, validates, ValidationError, fields, validate, validates_schema
import logging
from sqlalchemy import func

class UserSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = User
        load_instance = True
        exclude=("_password_hash",)
        
    patterns = fields.Nested(
        "PatternSchema",
        many=True,
        only=("id",),
    )
    
    purchases = fields.Nested(
        "PurchaseSchema",
        many=True,
        exclude=("user",),
        only=("id",),
    )
    
    # username = fields.String(required=True, validate=validate.Length(min=2,max=20))
    # email = fields.String(required=True, validate=[validate.Email()])
    # password_hash = fields.String(data_key="password_hash", required=True, validate=validate.Length(min=5), load_only=True)

    username = fields.String(required=True, validate=validate.Length(min=2, max=20), 
                            error_messages={"required": "Username is required.",
                                            "validate.Length": "Username must be between 2 and 20 characters long."})
    email = fields.String(required=True, validate=[validate.Email()],
                        error_messages={"required": "Email is required.",
                                        "validate.Email": "Invalid email format."})
    password_hash = fields.String(data_key="password_hash", required=True, 
                                validate=[validate.Length(min=8), validate.Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
                                                        error='Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.')], load_only=True,
                                error_messages={"required": "Password is required.",
                                                "validate.Length": "Password must be at least 8 characters long.", 
                                                "validate.Regexp": "Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character."})
    avatar = fields.String()


    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")
        existing_user = User.query.filter(func.lower(User.email) == func.lower(email)).first()
        if existing_user:
            raise ValidationError("Inputted email already exists.")
    
    def load(self, data, instance=None, *, partial=False, **kwargs):
        loaded_instance = super().load(
            data, instance=instance, partial=partial, **kwargs
        )
        for key, value in data.items():
            # if hasattr(loaded_instance, key):
            setattr(loaded_instance, key, value)
        return loaded_instance

user_schema = UserSchema()
users_schema = UserSchema(many=True)