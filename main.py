from fastapi import FastAPI
import json
import random


app = FastAPI()

with open("data.json",mode="r",encoding="utf-8") as file:
        x = json.load(file)

@app.get("/random")
def random_word():
    random_quota = random.choice(x)
    return random_quota

# with open("words.txt", mode="r") as file:
#     content = [j.split(';') for j in [i.strip() for i in file.readlines()]]
#     json = [{"word":i[0].strip(),"translation":i[1].strip(), "difficulty": 1} for i in content]