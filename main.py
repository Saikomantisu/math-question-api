from fastapi import FastAPI
from typing import Optional
from random_question import randomquestion
import json

app = FastAPI()

with open("./questions.json", "r") as f:
    questions = json.loads(f.read())

valid_levels = ["easy", "medium", "hard"]

# Route gốc để tránh lỗi 404
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def api(level: Optional[str] = None, limit: Optional[int] = None):
    if not level:
        return questions

    if level.lower() not in valid_levels:
        return {"Error": "Enter a valid level!", "Valid Levels": ["easy", "medium", "hard"]}

    filter_method = lambda list: list["level"] == level.upper()
    return list(filter(filter_method, questions))[0 : limit]

@app.get("/api/random")
def random_question(level: Optional[str] = None):
    while True:
        question = randomquestion()

        if not level:
            return question

        if level.lower() in valid_levels:
            if question["level"] == level.upper():
                return question
        else:
            return {"Error": "Enter a valid level!", "Valid Levels": ["easy", "medium", "hard"]}
