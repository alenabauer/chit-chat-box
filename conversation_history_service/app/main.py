from fastapi import FastAPI

from api.conversations import conversations

app = FastAPI()

app.include_router(conversations, prefix="/api/v1/conversations")