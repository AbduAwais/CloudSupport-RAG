from sqlalchemy.ext.asyncio import AsyncSession


class ConversationService:
    """Placeholder — methods to be implemented"""

    @staticmethod
    async def create_conversation(conversation, db: AsyncSession):
        pass

    @staticmethod
    async def get_conversation(conversation_id: int, db: AsyncSession):
        pass

    @staticmethod
    async def update_conversation(conversation_id: int, conversation, db: AsyncSession):
        pass

    @staticmethod
    async def delete_conversation(conversation_id: int, db: AsyncSession):
        pass
