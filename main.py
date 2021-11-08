from fastapi import FastAPI
from fastapi import status

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