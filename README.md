# CIOS (Adaptive Care Commercial Intelligence Operating System)

CIOS is a Commercial Intelligence Operating System designed to help organizations collect, validate, enrich, score, and activate commercial intelligence through a modular monolith architecture.

## Technology Stack

* Backend: FastAPI
* Frontend: Next.js (to be added)
* Database: PostgreSQL (coming in Sprint 1 Story 1.2)
* Cache & Queue: Redis (coming later)
* Object Storage: S3-compatible storage (coming later)

## Project Structure

```
cios/
├── backend/
├── frontend/      # Coming soon
└── README.md
```

## Current Progress

* ✅ Git initialized
* ✅ FastAPI configured
* ✅ Development environment ready
* ✅ Interactive API documentation available

## Running the Backend

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload
```

Open:

* http://127.0.0.1:8000
* http://127.0.0.1:8000/docs
