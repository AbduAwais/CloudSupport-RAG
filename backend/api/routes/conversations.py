import fastapi
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from models.conversation import Conversation, ConversationCreate, ConversationUpdate
from services.conversation_service import ConversationService

router = fastapi.APIRouter(prefix="/conversations", tags=["conversations"])

@router.post("/", response_model=Conversation)
async def create_conversation(conversation: ConversationCreate, db: AsyncSession = fastapi.Depends(get_db)):
    return await ConversationService.create_conversation(conversation, db)

@router.get("/{conversation_id}", response_model=Conversation)
async def get_conversation(conversation_id: int, db: AsyncSession = fastapi.Depends(get_db)):
    return await ConversationService.get_conversation(conversation_id, db)

@router.put("/{conversation_id}", response_model=Conversation)
async def update_conversation(conversation_id: int, conversation: ConversationUpdate, db: AsyncSession = fastapi.Depends(get_db)):
    return await ConversationService.update_conversation(conversation_id, conversation, db)

@router.delete("/{conversation_id}")
async def delete_conversation(conversation_id: int, db: AsyncSession = fastapi.Depends(get_db)):
    await ConversationService.delete_conversation(conversation_id, db)
    return {"message": "Conversation deleted successfully"}