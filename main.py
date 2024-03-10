from fastapi import FastAPI, Query
import json
import random


app = FastAPI(
    title="Gwara Wlkp API"
)

with open("data.json",mode="r",encoding="utf-8") as file:
        data = json.load(file)

@app.get("/all")
def get_all():
    return data

@app.get("/")
def main(amount: int = Query(1, title="amount", description="Amount of needed phrases"), level: int = Query(1, title="difficulty", description="Level of phrases difficulty")):
    phrases = random.choices([i for i in data if i['difficulty']==level], k=amount)
    return phrases


@app.get("/questions/")
def get_questions(questionAmount: int = Query(1, title="questionAmount", description="Amount of questions to generate"),
                  questionLevel: int = Query(1, title="questionLevel", description="Difficulty level of questions (1-3)")):

    # Filter phrases based on the specified difficulty level
    filtered_data = [phrase for phrase in data if phrase["difficulty"] == questionLevel]

    # Ensure the requested amount of questions doesn't exceed the available data
    questionAmount = min(questionAmount, len(filtered_data))

    questions = []
    for _ in range(questionAmount):
        phrase = random.choice(filtered_data)
        correct_translation = phrase["translation"]
        
        # Select two random wrong choices
        wrong_choices = random.sample([p["translation"] for p in data if p["translation"] != correct_translation], 2)

        # Create question with correct answer and two wrong choices
        question = {
            "word": phrase["word"],
            "options": {
                "a": correct_translation,
                "b": wrong_choices[0],
                "c": wrong_choices[1]
            }
        }
        questions.append(question)

    return questions
