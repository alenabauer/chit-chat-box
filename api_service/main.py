from fastapi import APIRouter
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv
load_dotenv()

class Question(BaseModel):
    question: str

router = APIRouter()
api_url = os.environ.get("API_URL")

@router.post("/ask_question")
def ask(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # make an HTTP request the answer-matching service to retrieve the best matching answer
    response = httpx.post(f"{api_url}/answer_matching_service/find_answer", json={"question": user_question})
    matching_answer = response.json()

    # create a JSON response with the best matching answer
    response = {"answer": matching_answer}

    return response