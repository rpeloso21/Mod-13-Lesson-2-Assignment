from marshmallow import fields, validate
from schema import ma

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False)
    product_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)
    employee_id = fields.Integer(required=True)



production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)
