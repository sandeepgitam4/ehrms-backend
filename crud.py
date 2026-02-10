from sqlalchemy.orm import Session
from models import Employee, Attendance
import random
import string

def generate_employee_id(db: Session):
    while True:
        emp_id = 'EMP' + ''.join(random.choices(string.digits, k=5))
        if not db.query(Employee).filter(Employee.employee_id == emp_id).first():
            return emp_id

def create_employee(db: Session, emp):
    employee_data = emp.dict()
    employee_data['employee_id'] = generate_employee_id(db)
    employee = Employee(**employee_data)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employee(db: Session, emp_id):
    return db.query(Employee).filter(Employee.employee_id == emp_id).first()

def get_employees(db: Session):
    return db.query(Employee).all()

def delete_employee(db: Session, emp_id: str):
    # 1. delete attendance records first
    db.query(Attendance).filter(
        Attendance.employee_id == emp_id
    ).delete(synchronize_session=False)

    # 2. delete employee
    employee = db.query(Employee).filter(
        Employee.employee_id == emp_id
    ).first()

    if employee:
        db.delete(employee)
        db.commit()

    return employee


def mark_attendance(db: Session, att):
    attendance = Attendance(**att.dict())
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

def get_attendance(db: Session, emp_id):
    return db.query(Attendance).filter(Attendance.employee_id == emp_id).all()

def get_all_attendance(db: Session):
    results = db.query(
        Attendance.employee_id,
        Attendance.date,
        Attendance.status,
        Employee.full_name
    ).join(Employee, Attendance.employee_id == Employee.employee_id).all()
    
    return [
        {
            'employee_id': r.employee_id,
            'date': r.date,
            'status': r.status,
            'full_name': r.full_name
        }
        for r in results
    ]
