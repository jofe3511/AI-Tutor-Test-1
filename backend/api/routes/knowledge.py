from fastapi import APIRouter

from backend.knowledge.schemas import KnowledgeStatus

router = APIRouter()


@router.get("/status", response_model=KnowledgeStatus)
def knowledge_status() -> KnowledgeStatus:
    return KnowledgeStatus(
        ingestion_ready=False,
        supported_sources=["pdf", "pptx", "docx", "txt", "md"],
        next_step="Add document upload, extraction, chunking, embeddings, and vector search.",
    )
