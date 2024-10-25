from sqlalchemy.orm import Session
from database import db
from models.employee import Employee
from models.production import Production
from circuitbreaker import circuit
from sqlalchemy import select


def fallback_function(production):
    return None


@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(production_data):

    try:
        if production_data['quantity_produced'] == 0:
            raise Exception("Failure condition triggered")
        with Session(db.engine) as session:
            with session.begin():
                new_production = Production(product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=production_data['date_produced'], employee_id=production_data['employee_id'])
                session.add(new_production)
                session.commit()
            session.refresh(new_production)
            return new_production
        
    except Exception as e:
        raise e
    
def find_all():
    query = select(Production)
    productions = db.session.execute(query).scalars().all()
    return productions


def find_employee_production():
    query = select(Production).join(Employee).where(Production.employee_id == Employee.id)
    employee_production = db.session.execute(query).scalars().all()
    return employee_production