# CIOS Backend

This directory contains the FastAPI backend for CIOS.

## Responsibilities

* Authentication
* Workspace management
* REST API
* Business logic
* Database access
* Background jobs

## Start Development Server

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run:

```bash
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs
