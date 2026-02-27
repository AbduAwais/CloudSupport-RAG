import chromadb
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# ChromaDB 
def get_chroma_client():
    """Initialize and return ChromaDB client"""
    return chromadb.PersistentClient(path="chroma_db")


def get_collection(client):
    """Get or create the files collection"""
    return client.get_or_create_collection(name="files_collection")


#  PostgreSQL 


DATABASE_URL = "postgresql+asyncpg://dkAbAwAh@localhost/cloudsupport_rag"
SYNC_DATABASE_URL = "postgresql://dkAbAwAh@localhost/cloudsupport_rag"

engine = create_async_engine(DATABASE_URL)
sync_engine = create_engine(SYNC_DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    """Create an async database session and close it when done"""
    async with AsyncSessionLocal() as db:
        yield db