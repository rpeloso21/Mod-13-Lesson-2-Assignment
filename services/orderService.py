from models.customer import Customer
from models.order import Order
from models.product import Product
from database import db
from sqlalchemy import select
from sqlalchemy.orm import Session

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'], total_price=order_data['total_price'])
            session.add(new_order)
            session.commit()
        session.refresh(new_order)
        return new_order
    
def find_all():
    query = select(Order)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_all_pagination(page=1, per_page=10):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders