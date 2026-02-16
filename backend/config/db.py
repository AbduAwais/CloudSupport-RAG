import chromadb

def get_chroma_client():
    """Initialize and return ChromaDB client"""
    return chromadb.PersistentClient(path="chroma_db")


def get_collection(client):
    """Get or create the files collection"""
    return client.get_or_create_collection(name="files_collection")