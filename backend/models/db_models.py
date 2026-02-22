from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from config.db import Base
import datetime

class ConversationDb(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    messages = relationship("MessageDB", back_populates="conversation")


class MessageDB(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    role = Column(String)
    content = Column(Text)
    conversation = relationship("ConversationDb", back_populates="messages")
    source_documents = Column(JSON, default=[])
    answer = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)