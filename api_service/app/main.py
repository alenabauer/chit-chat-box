from fastapi import FastAPI

from api.questions import questions

app = FastAPI()

app.include_router(questions, prefix="/api/v1/questions")