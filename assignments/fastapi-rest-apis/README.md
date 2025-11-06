# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework. Students will learn how to define routes, use Pydantic models for request/response validation, and run a development server with automatic API docs.

## 📝 Tasks

### 🛠️	Create a CRUD REST API

#### Description
Implement a small CRUD API (Create, Read, Update, Delete) for a simple resource (for example, "items" or "notes"). The API should validate input using Pydantic models, use an in-memory store for data, and be documented via the automatic OpenAPI docs that FastAPI provides.

#### Requirements
Completed project should:

- Expose REST endpoints for at least: list resources, get single resource by id, create resource, update resource, and delete resource
- Use Pydantic models for request validation and response schemas
- Return appropriate HTTP status codes (e.g., 201 for created, 404 for not found)
- Include clear example requests/responses in the README or docstrings
- Start with `uvicorn` for development and present the auto-generated docs at `/docs`
- Keep the implementation dependency-free beyond FastAPI/uvicorn (no database required; use an in-memory dict)

#### Example endpoints

- GET /items
- GET /items/{item_id}
- POST /items
- PUT /items/{item_id}
- DELETE /items/{item_id}

### 🛠️	Optional Challenge: Tests & Docker

#### Description
Add unit tests for the API using `requests` or `httpx` and provide a `Dockerfile` to containerize the app.

#### Requirements

- Provide at least 3 tests covering create/read/update/delete happy paths
- Add a simple `Dockerfile` that installs dependencies and runs the app with `uvicorn` (optional)

---

## Starter files

This folder includes `starter-code.py` (a minimal FastAPI scaffold) and `requirements.txt` listing dependencies. Run the app locally with uvicorn as described below.

## How to run (dev)

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
uvicorn starter-code:app --reload --port 8000
```

3. Open the interactive API docs at: http://localhost:8000/docs
