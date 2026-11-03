# fittrack-phase-1


FitTrack – Fitness & Workout Management Platform

Project Overview

FitTrack is a full-stack fitness and workout management application developed using FastAPI and React.

The application helps users manage their fitness activities, track daily workouts, monitor calories burned, set fitness goals, and analyze their progress through visual dashboards.

The main objective of this project is to develop a real-world fitness tracking platform with secure authentication, workout management, progress monitoring, and data analytics.

Technology Stack

Backend

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Bcrypt Password Hashing

Frontend

- React.js
- Vite
- JavaScript
- HTML5
- CSS3
- Axios
- React Router
- Recharts

Project Structure

FitTrack/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── config.py
│   ├── auth.py
│   ├── workouts.py
│   ├── progress.py
│   ├── goals.py
│   ├── reports.py
│   ├── notifications.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── api.js
│       ├── index.css
│       ├── components/
│       └── pages/
│
├── .gitignore
└── README.md

Project Modules

MODULE 1: User Authentication

- User Registration API.
- User Login API.
- JWT-based authentication.
- Password hashing using bcrypt.
- Protected routes.
- Secure token storage using localStorage.

MODULE 2: Workout Management System

- Add new workouts.
- Edit existing workouts.
- Delete workouts.
- Fetch user-specific workouts.
- Manage workout categories:
  - Cardio
  - Strength
  - Yoga
- Track workout duration and calories burned.

MODULE 3: Daily Progress Tracking

- Calculate total daily workouts.
- Calculate total calories burned.
- Generate daily workout summaries.
- Display fitness statistics.
- Provide a daily progress dashboard.

MODULE 4: Goal Setting System

- Create fitness goals.
- Update current goal values.
- Track goal progress.
- Set goal deadlines.
- Support goal types:
  - Weight Loss
  - Muscle Gain
  - Steps
- Monitor goal completion status.

MODULE 5: Reports & Analytics

- Weekly workout summary.
- Monthly progress report.
- Calories burned tracking.
- Workout statistics.
- Visual progress charts.
- Fitness analytics dashboard.

MODULE 6: Notifications System

- Daily workout reminders.
- Goal progress alerts.
- Notification list.
- Read and unread notification status.
- Notification management.

Database Design

The application uses SQLite with SQLAlchemy ORM.

Users Table

- id
- username
- email
- hashed_password
- created_at

Workouts Table

- id
- user_id
- workout_name
- category
- duration
- calories_burned
- workout_date
- created_at

Progress Table

- id
- user_id
- total_workouts
- total_calories
- date

Goals Table

- id
- user_id
- goal_type
- target_value
- current_value
- deadline
- created_at

Notifications Table

- id
- user_id
- title
- message
- is_read
- created_at

Security Features

- JWT-based authentication.
- Password hashing using bcrypt.
- Protected API endpoints.
- User ownership validation.
- Input validation using Pydantic.
- Environment-based configuration.
- Secure access to user-specific data.

Installation and Setup

1. Clone the Repository

git clone https://github.com/your-username/FitTrack.git

2. Navigate to Backend

cd FitTrack/backend

3. Create Virtual Environment

python -m venv venv

4. Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

5. Install Backend Dependencies

pip install -r requirements.txt

6. Configure Environment Variables

Create a ".env" file using ".env.example".

Configure the database URL and JWT secret key.

7. Run FastAPI Server

uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs

Frontend Setup

1. Navigate to Frontend

Open another terminal:

cd FitTrack/frontend

2. Install Dependencies

npm install

3. Start React Development Server

npm run dev

Frontend URL:

http://localhost:5173

Application Features

- Secure user registration and login.
- Workout creation and management.
- Daily fitness activity tracking.
- Fitness goal management.
- Weekly and monthly reports.
- Interactive analytics dashboard.
- Notification management.
- Responsive React user interface.

Expected Deliverables

1. Complete FastAPI backend.
2. React frontend application.
3. JWT authentication system.
4. Workout tracking functionality.
5. Daily progress dashboard.
6. Fitness goal management.
7. Reports and analytics.
8. Notification system.
9. Database integration.
10. API documentation using Swagger.

Development Timeline

Project Duration: 2 Days

- Day 1: Modules 1, 2 and 3.
- Day 2: Modules 4, 5 and 6.
- Final testing and integration.

Future Enhancements

- Google Fit integration.
- Wearable device integration.
- AI-based workout recommendations.
- Diet and nutrition tracking.
- Advanced fitness reports.
- Real-time activity monitoring.

Conclusion

FitTrack provides a complete fitness management solution that helps users maintain their workout routines, monitor fitness progress, and achieve personal health goals.

This project demonstrates full-stack development skills, REST API development, database management, authentication, and frontend integration using FastAPI and React.

---

Project Name: FitTrack – Fitness & Workout Management Platform

Backend: FastAPI

Frontend: React.js

Database: SQLite

Duration: 2 Days
