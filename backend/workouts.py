
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Workout, User
from schemas import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from auth import get_current_user

router = APIRouter(prefix="/workouts", tags=["Workouts"])


# Add New Workout
@router.post("/", response_model=WorkoutResponse)
def add_workout(
    workout: WorkoutCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if workout.category not in ["Cardio", "Strength", "Yoga"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid workout category"
        )

    new_workout = Workout(
        user_id=current_user.id,
        workout_name=workout.workout_name,
        category=workout.category,
        duration=workout.duration,
        calories_burned=workout.calories_burned,
        workout_date=workout.workout_date
    )

    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)

    return new_workout


# Get All User Workouts
@router.get("/", response_model=list[WorkoutResponse])
def get_workouts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workouts = db.query(Workout).filter(
        Workout.user_id == current_user.id
    ).order_by(Workout.workout_date.desc()).all()

    return workouts


# Get Single Workout
@router.get("/{workout_id}", response_model=WorkoutResponse)
def get_workout(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workout = db.query(Workout).filter(
        Workout.id == workout_id,
        Workout.user_id == current_user.id
    ).first()

    if not workout:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    return workout


# Update Workout
@router.put("/{workout_id}", response_model=WorkoutResponse)
def update_workout(
    workout_id: int,
    workout_data: WorkoutUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workout = db.query(Workout).filter(
        Workout.id == workout_id,
        Workout.user_id == current_user.id
    ).first()

    if not workout:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    update_data = workout_data.model_dump(exclude_unset=True)

    if "category" in update_data:
        if update_data["category"] not in ["Cardio", "Strength", "Yoga"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid workout category"
            )

    for key, value in update_data.items():
        setattr(workout, key, value)

    db.commit()
    db.refresh(workout)

    return workout


# Delete Workout
@router.delete("/{workout_id}")
def delete_workout(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workout = db.query(Workout).filter(
        Workout.id == workout_id,
        Workout.user_id == current_user.id
    ).first()

    if not workout:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    db.delete(workout)
    db.commit()

    return {
        "message": "Workout deleted successfully"
    }
