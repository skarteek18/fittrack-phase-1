

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from auth import router as auth_router
from workouts import router as workouts_router
from progress import router as progress_router
from goals import router as goals_router
from reports import router as reports_router
from notifications import router as notifications_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="FitTrack API",
    description="Fitness and Workout Management Platform",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth_router)
app.include_router(workouts_router)
app.include_router(progress_router)
app.include_router(goals_router)
app.include_router(reports_router)
app.include_router(notifications_router)


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to FitTrack Fitness Platform",
        "status": "Running Successfully"
    }


# Health Check API
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "FitTrack"
    }
