# Python
from typing import List

# FastAPI
from fastapi import FastAPI
from fastapi import status

# Models
from models.tweet import Tweet
from models.UserBase import UserBase
from models.UserLogin import UserLogin
from models.User import User

app = FastAPI()

# Path Operation Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Register a User",
    description="It is sent an object of type user, to create a new account"
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Login a User",
    description="It is sent an object of type user, to login app"
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Get all Users",
    description="Show all users in List with User Object"
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Get a User",
    description="Show a User by id"
)
def show_a_users():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Delete a User",
    description="Delete a User by id"
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update a User",
    description="Update a User by id"
)
def update_a_user():
    pass

# Path Operation Tweets

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    tags=["Tweet"],
    description="Show all to tweets",
    summary="Get all twitts"
)
def show_all_tweets():
    pass

@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=["Tweet"],
    summary="Post a Tweet",
    description="It is sent an object of type Tweet, to create a new tweet for user"
)
def post_tweet():
    pass

@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweet"],
    summary="Show a Tweet",
    description="Get Tweet by id"
)
def show_a_tweet():
    pass

@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweet"],
    summary="Delete a Tweet",
    description="Delete a Tweet by ID"
)
def delete_a_tweet():
    pass

@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweet"],
    summary="Update a Tweet",
    description="Update a Tweet by ID"
)
def update_a_tweet():
    pass