
from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional


# 1. User Registration Schema
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)


# User Response Schema
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# 2. User Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# 3. Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str


# 4. Workout Schema
class WorkoutCreate(BaseModel):
    workout_name: str
    category: str
    duration: int = Field(..., gt=0)
    calories_burned: float = Field(..., ge=0)
    workout_date: date


class WorkoutUpdate(BaseModel):
    workout_name: Optional[str] = None
    category: Optional[str] = None
    duration: Optional[int] = Field(None, gt=0)
    calories_burned: Optional[float] = Field(None, ge=0)
    workout_date: Optional[date] = None


class WorkoutResponse(BaseModel):
    id: int
    user_id: int
    workout_name: str
    category: str
    duration: int
    calories_burned: float
    workout_date: date
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# 5. Progress Schema
class ProgressCreate(BaseModel):
    total_workouts: int = Field(default=0, ge=0)
    total_calories: float = Field(default=0, ge=0)
    date: date


class ProgressResponse(BaseModel):
    id: int
    user_id: int
    total_workouts: int
    total_calories: float
    date: date

    class Config:
        from_attributes = True


# 6. Goal Schema
class GoalCreate(BaseModel):
    goal_type: str
    target_value: float = Field(..., gt=0)
    current_value: float = Field(default=0, ge=0)
    deadline: date


class GoalUpdate(BaseModel):
    current_value: Optional[float] = Field(None, ge=0)
    target_value: Optional[float] = Field(None, gt=0)
    deadline: Optional[date] = None


class GoalResponse(BaseModel):
    id: int
    user_id: int
    goal_type: str
    target_value: float
    current_value: float
    deadline: date
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# 7. Notification Schema
class NotificationCreate(BaseModel):
    title: str
    message: str


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    is_read: bool
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Notification Read Status Schema
class NotificationUpdate(BaseModel):
    is_read: bool
