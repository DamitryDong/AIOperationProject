# OpsPilot

AI Operations Platform — Week 1: FastAPI backend + Next.js dashboard.

## Project structure

```
AiOperationProject/
├── backend/           # FastAPI API (Python)
├── frontend/          # Next.js dashboard (TypeScript)
└── docker-compose.yml # Postgres + Redis (coming soon)
```

## Prerequisites

- Node.js 18+
- Python 3.11+
- Git

## 1. Start the backend

Open a terminal:

```bash
cd backend
python -m venv venv

# Git Bash / Mac / Linux:
source venv/Scripts/activate

# Windows CMD:
# venv\Scripts\activate.bat

pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at **http://localhost:8000**

Interactive docs: **http://localhost:8000/docs**

## 2. Start the frontend

Open a **second** terminal:

```bash
cd frontend
npm install
npm run dev
```

Dashboard runs at **http://localhost:3000**

## What works today

- `GET /health` — API status check
- `GET /documents` — list saved documents
- `POST /documents` — create a document (in-memory for now)
- Dashboard shows API status and a simple document form

## Next steps

1. Add PostgreSQL (Docker Compose)
2. Persist documents in the database
3. Authentication + multi-tenant orgs
