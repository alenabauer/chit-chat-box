# Chit Chat Box

This is a conversational AI system built using Python 3.9+ and FastAPI. The system consists of three microservices: API Service, Answer Matching Service, and Conversation History Service. It allows users to ask questions and receive answers, find the best matching answers from a knowledge base, and store conversation history.

## Requirements

- Python 3.9+
- FastAPI
- Docker

## Installation

Clone the repository:

```bash
git clone https://github.com/alenabauer/chit-chat-box.git
cd chit-chat-box
```

## Usage

1. Run the microservices with Docker Compose:
```bash
docker-compose up
```

2. API documentation is now available at
- http://localhost:8001/docs for the Answer Matching Service
- http://localhost:8002/docs for the API Service
- http://localhost:8003/docs for the Conversation History Service

3. Send a request to the API service:

- via curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "What is a server?"}' http://localhost:8002/api/v1/questions/new
```
- or via the Swagger UI at http://localhost:8002/docs

The API Service will return a JSON response containing the best matching answer from the knowledge base.

4. All conversations are stored in the conversation history database. To view the conversation history, send a request to the Conversation History Service:

- via curl:
```bash
curl -X GET http://localhost:8003/api/v1/conversations/
```
- or via the Swagger UI at http://localhost:8003/docs

## Credits

This project was created using the following resources:
- https://fastapi.tiangolo.com/tutorial/
- https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
- https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc#creating-movie-service
- https://learnpython.com/blog/python-requirements-file/

