# Backend

The backend is the real engine of the tutor app.

Recommended direction:

- Python
- FastAPI
- PostgreSQL
- Vector search
- Provider-independent AI model adapter

This should start as a modular monolith: one backend codebase with clear folders, not a pile of microservices.

## Current starting point

This folder now includes a minimal FastAPI skeleton:

```text
backend/
  main.py
  requirements.txt
  api/
    router.py
    routes/
      health.py
      courses.py
      knowledge.py
      students.py
      tutor.py
      assessments.py
```

## Run locally

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/api/v1/health
http://127.0.0.1:8000/docs
```
