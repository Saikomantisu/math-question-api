import random

def randomquestion():
    def get_level(answer):
        if answer < 150:
            return "EASY"
        elif answer < 500:
            return "MEDIUM"
        else:
            return "HARD"


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
        "level": get_level(result),
        "answer": result
    }

    return question

if __name__ == "__main__":
    randomquestion()