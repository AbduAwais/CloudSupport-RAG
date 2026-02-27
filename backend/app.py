from fastapi import FastAPI
from api.routes.main import router
from api.routes.conversations import router as conversations_router
from fastapi.middleware.cors import CORSMiddleware
from config.db import Base, sync_engine
from models.db_models import ConversationDb, MessageDB
import uvicorn


app = FastAPI()
Base.metadata.create_all(bind=sync_engine)
app.include_router(router)
app.include_router(conversations_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
async def root():
    return {"message": "RAG API is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)