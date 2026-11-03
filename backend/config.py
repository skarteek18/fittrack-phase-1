
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application Configuration
APP_NAME = "FitTrack"
APP_VERSION = "1.0.0"

# Database Configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./fittrack.db"
)

# JWT Configuration
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "change-this-to-a-secure-random-secret"
)

ALGORITHM = os.getenv("ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
)
