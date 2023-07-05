from fastapi import FastAPI

from app.api.answers import answers

app = FastAPI()

app.include_router(answers, prefix="/api/v1/answers", tags=["answers"])