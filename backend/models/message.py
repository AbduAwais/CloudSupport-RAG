from pydantic import BaseModel
from typing import List, Optional


class Query(BaseModel):
    query: str
    query_id: Optional[str] = None
    top_k: int = 5
    conversation_id: Optional[str] = None


class Messages(BaseModel):
    query_id: Optional[str] = None
    source_documents: List[str]
    content: str
    answer: str
    results: List[dict]
    role: str