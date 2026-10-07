from pydantic import BaseModel


class KnowledgeStatus(BaseModel):
    ingestion_ready: bool
    supported_sources: list[str]
    next_step: str
