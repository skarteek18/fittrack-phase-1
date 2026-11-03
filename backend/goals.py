
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from database import get_db
from models import Goal, User
from schemas import GoalCreate, GoalUpdate, GoalResponse
from auth import get_current_user

router = APIRouter(prefix="/goals", tags=["Fitness Goals"])


# Create New Goal
@router.post("/", response_model=GoalResponse)
def create_goal(
    goal: GoalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if goal.goal_type not in ["Weight Loss", "Muscle Gain", "Steps"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid goal type"
        )

    if goal.current_value >= goal.target_value:
        raise HTTPException(
            status_code=400,
            detail="Current value must be less than target value"
        )

    if goal.deadline < date.today():
        raise HTTPException(
            status_code=400,
            detail="Deadline cannot be in the past"
        )

    new_goal = Goal(
        user_id=current_user.id,
        goal_type=goal.goal_type,
        target_value=goal.target_value,
        current_value=goal.current_value,
        deadline=goal.deadline
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)

    return new_goal


# Get All User Goals
@router.get("/", response_model=list[GoalResponse])
def get_goals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goals = db.query(Goal).filter(
        Goal.user_id == current_user.id
    ).order_by(Goal.created_at.desc()).all()

    return goals


# Update Goal Progress
@router.put("/{goal_id}", response_model=GoalResponse)
def update_goal(
    goal_id: int,
    goal_data: GoalUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goal = db.query(Goal).filter(
        Goal.id == goal_id,
        Goal.user_id == current_user.id
    ).first()

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    update_data = goal_data.model_dump(exclude_unset=True)

    if "target_value" in update_data:
        if update_data["target_value"] <= 0:
            raise HTTPException(
                status_code=400,
                detail="Target value must be greater than zero"
            )

    new_target = update_data.get("target_value", goal.target_value)
    new_current = update_data.get("current_value", goal.current_value)

    if new_current > new_target:
        raise HTTPException(
            status_code=400,
            detail="Current value cannot exceed target value"
        )

    if "deadline" in update_data:
        if update_data["deadline"] < date.today():
            raise HTTPException(
                status_code=400,
                detail="Deadline cannot be in the past"
            )

    for key, value in update_data.items():
        setattr(goal, key, value)

    db.commit()
    db.refresh(goal)

    return goal


# Get Goal Progress and Status
@router.get("/{goal_id}/status")
def get_goal_status(
    goal_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goal = db.query(Goal).filter(
        Goal.id == goal_id,
        Goal.user_id == current_user.id
    ).first()

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    if goal.current_value >= goal.target_value:
        status = "COMPLETED"

    elif goal.deadline < date.today():
        status = "EXPIRED"

    else:
        status = "IN_PROGRESS"

    progress_percentage = min(
        (goal.current_value / goal.target_value) * 100,
        100
    )

    return {
        "goal_id": goal.id,
        "goal_type": goal.goal_type,
        "target_value": goal.target_value,
        "current_value": goal.current_value,
        "progress_percentage": round(progress_percentage, 2),
        "status": status,
        "deadline": goal.deadline
    }


# Delete Goal
@router.delete("/{goal_id}")
def delete_goal(
    goal_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goal = db.query(Goal).filter(
        Goal.id == goal_id,
        Goal.user_id == current_user.id
    ).first()

    if not goal:
        raise HTTPException(
            status_code=404,
            detail="Goal not found"
        )

    db.delete(goal)
    db.commit()

    return {
        "message": "Goal deleted successfully"
    }
