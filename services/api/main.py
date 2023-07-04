from fastapi import FastAPI
from pydantic import BaseModel

class Question(BaseModel):
    question: str

app = FastAPI()

@app.post("/ask")
def ask(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    # find the best matching answer from the knowledge base
    best_matching_answer = find_best_matching_answer(user_question)

    # create a JSON response with the best matching answer
    response = {"answer": best_matching_answer}

    return response

def find_best_matching_answer(question):
    # TODO: find the best matching answer from the knowledge base

    return "This is the best matching answer."