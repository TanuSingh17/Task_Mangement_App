# Task Management App
A simple Task Management API built using FastAPI and SQLAlchemy.

## Features
* Create a task
* View all tasks
* Update a task
* Delete a task
* User authentication using JWT
* Authorization

## Technologies Used
* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* JWT Authentication

## Installation

1. Clone the repository
git clone <repository-url>

2. Create a virtual environment
python -m venv env

3. Activate the virtual environment
env\Scripts\activate

4. Install dependencies
pip install -r requirement.txt

5. Configure environment variables in `.env`

6. Run database migrations
alembic upgrade head

7. Start the application
uvicorn main:app --reload
     or
fastapi dev main.py

## API Documentation
After starting the server, open:
* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`



