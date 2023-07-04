from fastapi import APIRouter

from pydantic import BaseModel

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/find_answer")
def find_best_matching_answer(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # TODO: find the best matching answer from the knowledge base
    best_matching_answer = "Connected to the answer-matching service"

    # create a JSON response with the best matching answer
    response = {"answer": best_matching_answer}

    return response