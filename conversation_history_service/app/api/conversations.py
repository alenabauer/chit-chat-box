from fastapi import APIRouter
from api.models import Conversation

conversations = APIRouter()

@conversations.get("/")
def get_all_conversations():
    print("Retrieving all conversations...")
    # TODO: retrieve all conversations from the database

@conversations.post("/new")
def save_conversation(conversation: Conversation):
    # retrieve the conversation from the request payload
    new_conversation = conversation.conversation
    print("Saving conversation to the database...")
    # TODO: save conversation to the database
