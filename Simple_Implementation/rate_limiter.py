import time

from fastapi import Depends, HTTPException, status

from auth import get_current_user
from schemas import User
from settings import RATE_LIMIT_CALLS, RATE_LIMIT_WINDOW, rate_limit_store


def check_rate_limit(user: User = Depends(get_current_user)) -> User:
    """Simple sliding window limiter to keep requests in check."""
    now = time.time()
    history = rate_limit_store[user.username]
    rate_limit_store[user.username] = [t for t in history if now - t < RATE_LIMIT_WINDOW]

    if len(rate_limit_store[user.username]) >= RATE_LIMIT_CALLS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Max {RATE_LIMIT_CALLS} requests per {RATE_LIMIT_WINDOW} seconds.",
        )

    rate_limit_store[user.username].append(now)
    return user
