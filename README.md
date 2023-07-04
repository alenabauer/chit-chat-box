# Chit Chat Box

This is a conversational AI system built using Python 3.9+ and FastAPI. The system consists of three microservices: API Service, Answer Matching Service, and Conversation History Service. It allows users to ask questions and receive answers, find the best matching answers from a knowledge base, and store conversation history.

## Requirements

- Python 3.9+
- FastAPI
- Docker (optional, for running with Docker Compose)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/alenabauer/chit-chat-box.git
cd chit-chat-box
```

2. Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Repeat step 2 for each of the three microservices.

## Usage

1. Run the app:
```bash
uvicorn main:app --reload
```

2. Send a request to the API service:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "What is VR"}' http://localhost:8000/api_service/ask_question
```
The API Service will return a JSON response containing the best matching answer from the knowledge base.

## Docker Compose

TODO

## Credits

This project was created using the following resources:
- https://fastapi.tiangolo.com/tutorial/
- https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
- https://learnpython.com/blog/python-requirements-file/
