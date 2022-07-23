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

# with open("words.txt", mode="r") as file:
#     content = [j.split(';') for j in [i.strip() for i in file.readlines()]]
#     json = [{"word":i[0].strip(),"translation":i[1].strip(), "difficulty": 1} for i in content]