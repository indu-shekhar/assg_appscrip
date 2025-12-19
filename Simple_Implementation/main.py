from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordRequestForm

from auth import create_access_token, verify_password
from rate_limiter import check_rate_limit
from schemas import Token, User
from services import analyze_with_gemini, search_market_data
from settings import users_db

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyzes market data for specific sectors in India using GenAI.",
    version="1.0.0",
)


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login to receive a JWT bearer token."""
    user_dict = users_db.get(form_data.username)
    if not user_dict or not verify_password(form_data.password, user_dict["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user_dict["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/analyze/{sector}", response_class=PlainTextResponse)
async def analyze_sector(sector: str, user: User = Depends(check_rate_limit)):
    """Analyze a sector after auth and rate checks."""
    if not sector or len(sector) < 3:
        raise HTTPException(status_code=400, detail="Invalid sector name provided.")

    market_data = search_market_data(sector)
    try:
        analysis_report = analyze_with_gemini(sector, market_data)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    return analysis_report


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)