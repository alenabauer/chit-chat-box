from fastapi import APIRouter
from api.models import Conversation

conversations = APIRouter()

@conversations.get("/")
def get_all_conversations():
    print("Retrieving all conversations...")
    # TODO: retrieve all conversations from the database

@conversations.post("/new")
def save_conversation(conversation: Conversation):
    print("Saving conversation to the database...")
    print(conversation)
    # TODO: save conversation to the database
    return "Conversation saved successfully!"
