from fastapi import FastAPI
from api_service.main import router as api_service_router
from answer_matching_service.main import router as answer_matching_router

# TODO: refactor and use app instead of router for each microservice

app = FastAPI()

app.include_router(api_service_router, prefix="/api_service")
app.include_router(answer_matching_router, prefix="/answer_matching_service")