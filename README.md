# HRMS Lite - Backend

Employee Management System Backend built with FastAPI and PostgreSQL.

## Features
- Employee Management (CRUD operations)
- Attendance Tracking
- Auto-generated Employee IDs
- RESTful API

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Python 3.11+

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set DATABASE_URL environment variable

3. Run the application:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `POST /create_employee` - Create new employee
- `GET /get_employees` - Get all employees
- `GET /get_employee/{employee_id}` - Get single employee
- `DELETE /employees/{employee_id}` - Delete employee
- `POST /mark_attendance` - Mark attendance
- `GET /get_attendance/{employee_id}` - Get employee attendance
- `GET /get_all_attendance` - Get all attendance records

## Environment Variables

- `DATABASE_URL` - PostgreSQL connection string
- `FRONTEND_URL` - Frontend URL for CORS (optional)
