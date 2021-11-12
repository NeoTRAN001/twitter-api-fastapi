# Pydantic
from pydantic import Field

# Models
from .user import User

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )