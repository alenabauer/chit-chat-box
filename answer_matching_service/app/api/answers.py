from fastapi import APIRouter
from app.api.models import Question
import json

def load_knowledge_base():
    with open("app/resources/knowledge_base.json") as file:
        kb_data = json.load(file)
        kb_answers = list(kb_data.values())
    return kb_answers

kb_answers = load_knowledge_base()
# TODO: look into dependency injection: https://www.fastapitutorial.com/blog/dependency-injection-fastapi/

answers = APIRouter()

# TODO: use typing consistently
# look into different storage types

@answers.post("/", status_code=201)
def find_best_matching_answer(question: Question):
    user_question = question.question
    best_matching_answer = search_knowledge_base(user_question)
    response = {"answer": best_matching_answer}
    return response

def search_knowledge_base(user_question):
    best_matching_answer = ""
    best_similarity_score = 0.0

    for kb_answer in kb_answers:
        similarity_score = jaccard_similarity(user_question, kb_answer)

        if similarity_score > best_similarity_score:
            best_similarity_score = similarity_score
            best_matching_answer = kb_answer

    return best_matching_answer

# source: https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)