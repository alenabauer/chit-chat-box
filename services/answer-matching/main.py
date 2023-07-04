from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/match")
def find_best_matching_answer(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # TODO: find the best matching answer from the knowledge base
    best_matching_answer = "This is the best matching answer."

    # create a JSON response with the best matching answer
    response = {"answer": best_matching_answer}

    return response