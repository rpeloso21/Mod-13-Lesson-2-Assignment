from marshmallow import fields
from schema import ma

class CustomerSchema(ma.Schema):
    id = fields.Integer(required = False)
    name = fields.String(required = True)
    email = fields.String(required = True)
    phone = fields.String(required = True)

    class Meta:
        fields = ("id", "name", "email", "phone")


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)