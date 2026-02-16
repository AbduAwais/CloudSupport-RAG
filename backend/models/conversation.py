from pydantic import BaseModel
from typing import List, Optional
from backend.models.chat import Messages



class Conversation(BaseModel):
    conversation_id: Optional[str] = None
    messages: List[Messages]
    created_at: Optional[str] = None
    title: Optional[str] = None



### her kenne vil jeg lave nogle response models senere, men dog ikke nu.