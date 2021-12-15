import random


def randomquestion():
    def get_level(answer):
        if answer < 150:
            wrong1 = answer - 1
            wrong2 = answer - 5
            wrong3 = answer - 50
            return {"level": "EASY", "wrong": [wrong1, wrong2, wrong3]}
        elif answer < 500:
            wrong1 = answer - 100
            wrong2 = answer - 52
            wrong3 = answer - 42
            return {"level": "MEDIUM", "wrong": [wrong1, wrong2, wrong3]}
        else:
            wrong1 = answer - 250
            wrong2 = answer - 30
            wrong3 = answer - 11
            return {"level": "HARD", "wrong": [wrong1, wrong2, wrong3]}

    operators = ["+", "-", "x"]

    num1 = random.randrange(1, 400, 1)
    num2 = random.randrange(1, 100, 2)
    operator = random.choice(operators)

    calculate = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "x": lambda x, y: x * y,
    }

    result = round(calculate[operator](num1, num2), 2)

    question = {
        "question": f"{num1} {operator} {num2}",
        "level": get_level(result)["level"],
        "answer": result,
        "wrong_answers": get_level(result)["wrong"]
    }

    return question


if __name__ == "__main__":
    randomquestion()
