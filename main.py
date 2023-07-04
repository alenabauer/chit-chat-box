from fastapi import FastAPI
from api_service.main import router as api_service_router
from answer_matching_service.main import router as answer_matching_router

app = FastAPI()

app.include_router(api_service_router, prefix="/api_service")
app.include_router(answer_matching_router, prefix="/answer_matching_service")

@app.get("/")
def read_root():
    return {"Hello": "World"}