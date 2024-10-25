from sqlalchemy.orm import Session
from database import db
from models.employee import Employee
from circuitbreaker import circuit
from sqlalchemy import select


def fallback_function(employee):
    return None


@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(employee_data):

    try:
        if employee_data['name'] == "Failure":
            raise Exception("Failure condition triggered")
        with Session(db.engine) as session:
            with session.begin():
                new_employee = Employee(name=employee_data['name'], position=employee_data['position'])
                session.add(new_employee)
                session.commit()
            session.refresh(new_employee)
            return new_employee
        
    except Exception as e:
        raise e
    
def find_all():
    query = select(Employee)
    employees = db.session.execute(query).scalars().all()
    return employees