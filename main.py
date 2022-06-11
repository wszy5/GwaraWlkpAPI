from fastapi import FastAPI
import json
import random

with open("data.json",mode="r") as file:
    x = json.load(file)
print(x)
app = FastAPI()
random_quota = random.choice(x)
@app.get("random")
def random_word():
    return(x[0])

# with open("words.txt", mode="r") as file:
#     content = [j.split(';') for j in [i.strip() for i in file.readlines()]]
#     json = [{"word":i[0].strip(),"translation":i[1].strip(), "difficulty": 1} for i in content]

# print(random.choice(x))
