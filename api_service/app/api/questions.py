from fastapi import APIRouter
from api.models import Question
import httpx

questions = APIRouter()

@questions.post("/new")
def ask(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # make an HTTP request the answer-matching service to retrieve the best matching answer
    # TODO: replace hardcoded URL with environment variable
    response = httpx.post("http://localhost:8000/api/v1/answers/find_best_match", json={"question": user_question})
    matching_answer = response.json()["answer"]

    # create a JSON response with the best matching answer
    response = {"answer": matching_answer}

    return response