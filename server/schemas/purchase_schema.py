from config import ma
from marshmallow import fields, validate
from models.purchase import Purchase

class PurchaseSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Purchase
        load_instance = True

    user = fields.Nested(
        "UserSchema",
        only=("id",),
    )

    user_id = fields.Integer(required=True, validate=validate.Range(min=1, error="Invalid user ID"))
    pattern_id = fields.Integer(required=True, validate=validate.Range(min=1, error="Invalid pattern ID"))
    price = fields.Float(required=True, validate=validate.Range(min=0, error="Price must be a positive number"))
    payment_method = fields.String(required=True)
    status = fields.String(required=True, validate=validate.OneOf(["Pending", "Completed", "Canceled"], error="Invalid status"))

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)