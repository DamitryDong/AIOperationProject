from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="OpsPilot API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store for Week 1 — replaced with PostgreSQL later
documents: list[dict] = []


class DocumentCreate(BaseModel):
    name: str
    content: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "OpsPilot API"}


@app.get("/documents")
def list_documents():
    return {"documents": documents}


@app.post("/documents")
def create_document(doc: DocumentCreate):
    record = {
        "id": len(documents) + 1,
        "name": doc.name,
        "content": doc.content,
    }
    documents.append(record)
    return record
