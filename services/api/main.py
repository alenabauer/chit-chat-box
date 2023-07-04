from fastapi import FastAPI
from pydantic import BaseModel

class Question(BaseModel):
    question: str

app = FastAPI()

@app.post("/ask")
def ask(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # TODO: connect to the answer-matching service and retrieve the best matching answer

    # create a JSON response with the best matching answer
    response = {"answer": "This is the best matching answer."}

    return response