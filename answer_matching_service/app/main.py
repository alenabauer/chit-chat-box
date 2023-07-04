from fastapi import FastAPI

from api.answers import answers

app = FastAPI()

app.include_router(answers, prefix="/api/v1/answers")