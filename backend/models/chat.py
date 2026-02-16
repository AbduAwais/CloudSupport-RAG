from pydantic import BaseModel
from typing import List, Optional


class Query(BaseModel):
    query: str
    query_id: Optional[str] = None
    top_k: Optional[int] = 5


class Messages(BaseModel):
    query_id: Optional[str] = None
    source_documents: List[dict]
    content: str
    answer: str
    results: List[dict]
    role = str