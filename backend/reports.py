
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta

from database import get_db
from models import Workout, User
from auth import get_current_user

router = APIRouter(prefix="/reports", tags=["Reports & Analytics"])


# Weekly Workout Summary
@router.get("/weekly")
def weekly_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    today = date.today()
    start_date = today - timedelta(days=6)

    workouts = db.query(Workout).filter(
        Workout.user_id == current_user.id,
        Workout.workout_date >= start_date,
        Workout.workout_date <= today
    ).all()

    total_workouts = len(workouts)

    total_calories = sum(
        workout.calories_burned for workout in workouts
    )

    total_duration = sum(
        workout.duration for workout in workouts
    )

    return {
        "report_type": "Weekly Report",
        "start_date": start_date,
        "end_date": today,
        "total_workouts": total_workouts,
        "total_calories": total_calories,
        "total_duration": total_duration
    }


# Monthly Progress Report
@router.get("/monthly")
def monthly_report(
    year: int = None,
    month: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    today = date.today()

    selected_year = year or today.year
    selected_month = month or today.month

    if selected_month < 1 or selected_month > 12:
        return {
            "error": "Month must be between 1 and 12"
        }

    start_date = date(selected_year, selected_month, 1)

    if selected_month == 12:
        end_date = date(selected_year + 1, 1, 1)
    else:
        end_date = date(selected_year, selected_month + 1, 1)

    query = db.query(Workout).filter(
        Workout.user_id == current_user.id,
        Workout.workout_date >= start_date,
        Workout.workout_date < end_date
    )

    if selected_year == today.year and selected_month == today.month:
        query = query.filter(Workout.workout_date <= today)

    workouts = query.all()

    total_workouts = len(workouts)

    total_calories = sum(
        workout.calories_burned for workout in workouts
    )

    total_duration = sum(
        workout.duration for workout in workouts
    )

    return {
        "report_type": "Monthly Report",
        "year": selected_year,
        "month": selected_month,
        "total_workouts": total_workouts,
        "total_calories": total_calories,
        "total_duration": total_duration
    }


# Calories Tracking
@router.get("/calories")
def calories_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    calorie_data = db.query(
        Workout.workout_date,
        func.sum(Workout.calories_burned).label("total_calories")
    ).filter(
        Workout.user_id == current_user.id
    ).group_by(
        Workout.workout_date
    ).order_by(
        Workout.workout_date
    ).all()

    return [
        {
            "date": item.workout_date,
            "total_calories": item.total_calories
        }
        for item in calorie_data
    ]


# Workout Category Analytics
@router.get("/categories")
def category_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    category_data = db.query(
        Workout.category,
        func.count(Workout.id).label("total_workouts"),
        func.sum(Workout.calories_burned).label("total_calories")
    ).filter(
        Workout.user_id == current_user.id
    ).group_by(
        Workout.category
    ).all()

    return [
        {
            "category": item.category,
            "total_workouts": item.total_workouts,
            "total_calories": item.total_calories or 0
        }
        for item in category_data
    ]
