
from config.db import get_chroma_client, get_collection

from fastapi import FastAPI

from models.message import Messages, Query

class RAGService:
    def __init__(self):
        self.chroma_client = get_chroma_client()
        self.collection = get_collection(self.chroma_client)

    def query(self, request: Query) -> Messages:
        """
        Query the RAG collection to retrieve relevant documents.
        
        Takes a Query request with a search term and returns matching documents
        and their metadata from ChromaDB. Flattens the nested list structure
        returned by ChromaDB to a flat list format for the Messages model.
        
        Args:
            request: Query object containing the search query and parameters
            
        Returns:
            Messages object with source documents, metadata, and query info
        """
        search_result = self.collection.query(
            query_texts=[request.query],
            n_results=request.top_k
        )
        flat_documents = search_result['documents'][0] if search_result['documents'] else []
        flat_results = [dict(m) for m in search_result['metadatas'][0]] if search_result['metadatas'] else []        
        return Messages(
            source_documents=flat_documents,
            content=request.query,
            answer="",
            results=flat_results,
            query_id=request.query_id,
            role="assistant",
        )