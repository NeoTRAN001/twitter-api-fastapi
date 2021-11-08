# Pydantic
from pydantic import Field

# Models
from UserBase import UserBase

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )