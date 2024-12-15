from flask import jsonify
from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from models.order import Order
from circuitbreaker import circuit
from sqlalchemy import select


def fallback_function(customer):
    return None


@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(customer_data):

    try:
        if customer_data['name'] == "Failure":
            raise Exception("Failure condition triggered")
        with Session(db.engine) as session:
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                session.add(new_customer)
                session.commit()
            session.refresh(new_customer)
            return new_customer
        
    except Exception as e:
        raise e
    
def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

def customer_value():
    # Perform the SQL query using SQLAlchemy
    result = db.session.query(
        Customer.name,
        db.func.sum(Order.total_price).label('total_cost')
    ).join(Order, Order.customer_id == Customer.id).group_by(Customer.name).having(db.func.sum(Order.total_price) > 1000).all()

    # Format the result as a list of dictionaries
    customer_totals = [{'name': row.name, 'total_cost': row.total_cost} for row in result]

    # Return the result as JSON
    return jsonify(customer_totals)