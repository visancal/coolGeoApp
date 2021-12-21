# Python
from typing import Optional, List

# Pydantic
from pydantic import BaseModel,Field


# Models

class LoginUsr(BaseModel):
    user: str = Field(...,min_length=6,max_length=25,example="visancal")
    password: str = Field(...,min_length=8,max_length=30,example="tfr45re432wD")


class UsrSession(BaseModel):
    user: str = Field(...)
    name: str
    token: str
    lang: str