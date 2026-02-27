from pydantic import BaseModel
from typing import List, Optional
from models.message import Messages


class ConversationCreate(BaseModel):
    title: Optional[str] = None
    created_at: Optional[str] = None



class Conversation(BaseModel):
    conversation_id: Optional[str] = None
    messages: List[Messages]
    created_at: Optional[str] = None
    title: Optional[str] = None

class ConversationUpdate(BaseModel):
    title: Optional[str] = None
    conversation_id: Optional[str] = None

### her kenne vil jeg lave nogle response models senere, men dog ikke nu.