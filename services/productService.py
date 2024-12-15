from flask import jsonify
from models.product import Product
from models.production import Production
from models.order import Order
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select


def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
    
def find_all():
    query = select(Product)
    products = db.session.execute(query).scalars().all()
    return products

def find_all_pagination(page=1, per_page=10):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

def top_selling_products():
    # Perform the SQL query using SQLAlchemy
    result = db.session.query(
        Product.name,
        db.func.sum(Order.quantity).label('total_quantity_ordered')
    ).join(Order, Order.product_id == Product.id).group_by(Product.name).all()

    # Format the result as a list of dictionaries
    product_totals = [{'name': row.name, 'total_quantity_ordered': row.total_quantity_ordered} for row in result]

    # Return the result as JSON
    return jsonify(product_totals)

def produced_by_date():
    # Perform the SQL query using SQLAlchemy
    subquery = db.session.query(Production.date_produced).filter(Production.date_produced == '2024-03-04').distinct()

    result = db.session.query(
        Product.name,
        db.func.sum(Production.quantity_produced).label('produced_by_date')
    ).join(Production, Production.product_id == Product.id).filter(Production.date_produced.in_(subquery)).group_by(Product.name).all()

    # Format the result as a list of dictionaries
    product_production = [{'name': row.name, 'produced_by_date': row.produced_by_date} for row in result]

    # Return the result as JSON
    return jsonify(product_production)