# Simple_Implementation

Minimal instructions to run the Trade Opportunities API locally.

Prerequisites
- Python 3.10+ recommended
- git (optional)

Setup
1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the example env and set your keys:

```bash
cp .env.example .env
# Edit .env and set GEMINI_API_KEY and SECRET_KEY
```

Run the app

From inside the `Simple_Implementation` folder (where `main.py` lives):

```bash
# Option A: run with the start script
./start.sh

# Option B: run uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Notes
- The app expects `GEMINI_API_KEY` in the environment to use the Gemini model.
- For testing, use username `developer` and password `secret` (hardcoded demo user).
