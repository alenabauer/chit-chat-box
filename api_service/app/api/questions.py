from fastapi import APIRouter
from app.api.models import Question
from datetime import datetime
import httpx
import os

questions = APIRouter()

# TODO: add error handling for when the environment variables are not set
answer_matching_host_url = os.environ.get('ANSWER_MATCHING_SERVICE_URL')
conversation_history_host_url = os.environ.get('CONVERSATION_HISTORY_SERVICE_URL')

@questions.post("/new", status_code=201)
def ask(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # make an HTTP request the answer-matching service to retrieve the best matching answer
    print("Sending a request to the answer-matching service...")
    # TODO: handle exceptions
    response = httpx.post(answer_matching_host_url, json={"question": user_question})
    matching_answer = response.json()["answer"]

    # Get the current time
    current_time = datetime.now().isoformat()

    conversation = {
        "question": user_question,
        "answer": matching_answer,
        "timestamp": current_time
    }

    # make an HTTP request to the conversation-history service to save the conversation
    print("Sending a request to the conversation-history service...")
    # TODO: handle exceptions
    response = httpx.post(conversation_history_host_url, json=conversation)

    # create a JSON response with the best matching answer
    response = {"answer": matching_answer}

    return response

# TODO: look into the logging module