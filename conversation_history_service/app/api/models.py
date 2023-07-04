from pydantic import BaseModel

class Conversation(BaseModel):
    question: str
    answer: str
    timestamp: str