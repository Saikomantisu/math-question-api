from fastapi import FastAPI
from typing import Optional
from random_question import randomquestion
import random
import json

app = FastAPI()

with open("./questions.json", "r") as f:
    questions = json.loads(f.read())

@app.get("/api")
def api():
    return questions

@app.get("/api/random")
def random_question(level : Optional[str] = None):
    valid_levels = ["easy", "medium", "hard"]

    while True:
        question = randomquestion()

        if not level:
            return question

        if level.lower() in valid_levels:
            if question["level"] == level.upper():
                return question
        else:
            return { "Error": "Enter a valid level!", "Valid Levels": ["easy", "medium", "hard"]}
        
