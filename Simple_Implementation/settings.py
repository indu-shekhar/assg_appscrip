import logging
import os
from collections import defaultdict

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Core configuration defaults; env vars take priority in real deployments.
SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key-change-me")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security primitives
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Demo user store
users_db = {
    "developer": {
        "username": "developer",
        "hashed_password": pwd_context.hash("secret"),
    }
}

# Rate limiting primitives
rate_limit_store = defaultdict(list)
RATE_LIMIT_CALLS = 5
RATE_LIMIT_WINDOW = 60  # seconds
