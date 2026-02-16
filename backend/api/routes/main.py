from fastapi import APIRouter, HTTPException
from models.message import Messages, Query
from services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()


@router.post("/query")
async def query_rag(request: Query) -> Messages:
    """
    Endpoint to handle RAG queries. Accepts a Query object with the search term
    and parameters, and returns a Messages object containing relevant documents,
    metadata, and query information.
    
    Args:
        request: Query object containing the search query and parameters
        
    Returns:
        Messages object with source documents, metadata, and query info
    """
    try:
        response = rag_service.query(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



