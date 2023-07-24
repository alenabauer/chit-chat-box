from fastapi import APIRouter
from app.api.models import Conversation
from app.api import db_manager

conversations = APIRouter()

@conversations.get("/")
async def index():
    print("Retrieving all conversations...")
    return await db_manager.get_all_conversations()

@conversations.post("/", status_code=201)
async def add_conversation(conversation: Conversation):
    print("Saving conversation to the database...")
    await db_manager.add_conversation(conversation)
    return "Conversation saved successfully!"

# TODO use logging module
# TODO add error handling
# ORM