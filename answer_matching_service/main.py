from fastapi import APIRouter
from pydantic import BaseModel
import json
import os

# TODO: refactor and use app instead of router for each microservice

# construct the path to the JSON file
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, 'knowledge_base.json')

# Open the JSON file
with open(json_file_path) as file:
    # Load the JSON data and extract all answers
    kb_data = json.load(file)
    kb_answers = list(kb_data.values())

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/find_answer")
def find_best_matching_answer(question: Question):
    # retrieve the question from the request payload
    user_question = question.question

    best_matching_answer = search_knowledge_base(user_question)

    # create a JSON response with the best matching answer
    response = {"answer": best_matching_answer}

    return response

def search_knowledge_base(user_question):
    # initialize variables to store the best matching answer and its similarity score
    best_matching_answer = ""
    best_similarity_score = 0.0

    # iterate through all answers in the knowledge base
    for kb_answer in kb_answers:
        # calculate the similarity score between the question and the answers in the knowledge base
        similarity_score = jaccard_similarity(user_question, kb_answer)

        # update the best matching question and its similarity score
        if similarity_score > best_similarity_score:
            best_similarity_score = similarity_score
            best_matching_answer = kb_answer

    return best_matching_answer

# source: https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
def jaccard_similarity(x,y):
    # returns the jaccard similarity between two lists
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)