from app.api.models import Conversation
from app.api.db import conversations, database

async def add_conversation(payload: Conversation):
    query = conversations.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_conversations():
    query = conversations.select()
    return await database.fetch_all(query=query)
