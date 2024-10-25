from models.product import Product
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