import chromadb
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ChromaDB 
def get_chroma_client():
    """Initialize and return ChromaDB client"""
    return chromadb.PersistentClient(path="chroma_db")


def get_collection(client):
    """Get or create the files collection"""
    return client.get_or_create_collection(name="files_collection")


#  PostgreSQL 


DATABASE_URL = "postgresql://dkAbAwAh@localhost/cloudsupport_rag"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    """Create a database session and close it when done"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()