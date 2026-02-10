from datetime import date
from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    full_name: str
    email: str
    department: str

class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: str
