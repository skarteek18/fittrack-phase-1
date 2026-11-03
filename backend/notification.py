
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from database import get_db
from models import Notification, Goal, Workout, User
from schemas import (
    NotificationCreate,
    NotificationUpdate,
    NotificationResponse
)
from auth import get_current_user

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# Create New Notification
@router.post("/", response_model=NotificationResponse)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_notification = Notification(
        user_id=current_user.id,
        title=notification.title,
        message=notification.message
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification


# Get All Notifications
@router.get("/", response_model=list[NotificationResponse])
def get_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    notifications = db.query(Notification).filter(
        Notification.user_id == current_user.id
    ).order_by(Notification.created_at.desc()).all()

    return notifications


# Mark Notification as Read
@router.put("/{notification_id}/read")
def mark_notification_read(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.is_read = True

    db.commit()
    db.refresh(notification)

    return {
        "message": "Notification marked as read"
    }


# Mark Notification as Unread
@router.put("/{notification_id}/unread")
def mark_notification_unread(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.is_read = False

    db.commit()

    return {
        "message": "Notification marked as unread"
    }


# Get Unread Notifications
@router.get("/unread")
def get_unread_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    notifications = db.query(Notification).filter(
        Notification.user_id == current_user.id,
        Notification.is_read == False
    ).order_by(Notification.created_at.desc()).all()

    return notifications


# Delete Notification
@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification deleted successfully"
    }


# Daily Workout Reminder
@router.post("/daily-reminder")
def daily_workout_reminder(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    today = date.today()

    today_workout = db.query(Workout).filter(
        Workout.user_id == current_user.id,
        Workout.workout_date == today
    ).first()

    if today_workout:
        message = "Great job! You have completed a workout today."

        title = "Workout Completed"

    else:
        message = "Stay active! Do not forget your daily workout."

        title = "Daily Workout Reminder"

    new_notification = Notification(
        user_id=current_user.id,
        title=title,
        message=message
    )

    db.add(new_notification)
    db.commit()

    return {
        "message": "Daily reminder created successfully"
    }


# Goal Progress Alert
@router.post("/goal-alert")
def goal_progress_alert(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goals = db.query(Goal).filter(
        Goal.user_id == current_user.id
    ).all()

    alerts = []

    for goal in goals:

        percentage = (
            goal.current_value / goal.target_value
        ) * 100

        if percentage >= 100:
            message = f"Congratulations! Your {goal.goal_type} goal is completed."

        elif percentage >= 75:
            message = f"Almost there! Your {goal.goal_type} goal is {percentage:.2f}% completed."

        else:
            continue

        new_notification = Notification(
            user_id=current_user.id,
            title="Fitness Goal Update",
            message=message
        )

        db.add(new_notification)

        alerts.append(message)

    db.commit()

    return {
        "message": "Goal alerts generated successfully",
        "alerts": alerts
    }
