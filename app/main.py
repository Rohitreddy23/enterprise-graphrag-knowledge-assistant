from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Enterprise GraphRAG Knowledge Assistant",
    description="A production-style GraphRAG API for enterprise document search and question answering.",
    version="1.0.0",
)

app.include_router(router, prefix="/api", tags=["GraphRAG"])


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "enterprise-graphrag-knowledge-assistant"}
