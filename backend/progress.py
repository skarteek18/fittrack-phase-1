
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from database import get_db
from models import Workout, Progress, User
from schemas import ProgressResponse
from auth import get_current_user

router = APIRouter(prefix="/progress", tags=["Daily Progress"])


# Get Daily Progress
@router.get("/daily", response_model=ProgressResponse)
def get_daily_progress(
    progress_date: date = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    selected_date = progress_date or date.today()

    # Calculate total workouts
    total_workouts = db.query(Workout).filter(
        Workout.user_id == current_user.id,
        Workout.workout_date == selected_date
    ).count()

    # Calculate total calories
    total_calories = db.query(
        func.coalesce(func.sum(Workout.calories_burned), 0)
    ).filter(
        Workout.user_id == current_user.id,
        Workout.workout_date == selected_date
    ).scalar()

    # Find existing progress
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.date == selected_date
    ).first()

    # Create or update progress
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            total_workouts=total_workouts,
            total_calories=total_calories,
            date=selected_date
        )

        db.add(progress)

    else:
        progress.total_workouts = total_workouts
        progress.total_calories = total_calories

    db.commit()
    db.refresh(progress)

    return progress


# Get Complete Progress History
@router.get("/history", response_model=list[ProgressResponse])
def get_progress_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    progress_list = db.query(Progress).filter(
        Progress.user_id == current_user.id
    ).order_by(Progress.date.desc()).all()

    return progress_list


# Get Overall Fitness Summary
@router.get("/summary")
def get_fitness_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    total_workouts = db.query(Workout).filter(
        Workout.user_id == current_user.id
    ).count()

    total_calories = db.query(
        func.coalesce(func.sum(Workout.calories_burned), 0)
    ).filter(
        Workout.user_id == current_user.id
    ).scalar()

    total_duration = db.query(
        func.coalesce(func.sum(Workout.duration), 0)
    ).filter(
        Workout.user_id == current_user.id
    ).scalar()

    return {
        "total_workouts": total_workouts,
        "total_calories": total_calories,
        "total_duration": total_duration
    }
