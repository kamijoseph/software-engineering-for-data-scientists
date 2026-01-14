
# chapter 11: APIs
from fastapi import FastAPI

# intialise app
app = FastAPI()

# simple get endpoint
@app.get("/say_hi/")
def say_hi():
    return {
        "Hi": "There"
    }
