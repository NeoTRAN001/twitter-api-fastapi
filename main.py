# FastAPI
from fastapi import FastAPI
from fastapi import status

# Models
from models.User import User
from models.UserBase import UserBase
from models.UserLogin import UserLogin
from models.Tweet import Tweet

app = FastAPI()

@app.get(
    path="/",
    tags=["Home"],
    description="Home to Twitter API",
    summary="Get all twitts",
    status_code=status.HTTP_200_OK
)
def home():
    return {
        "Twitter API": "Working!"
    }