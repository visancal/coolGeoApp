
# Python
from typing import Optional, List 

# Pydantic
from pydantic import BaseModel,Field

# Models

class RangeGender(BaseModel):
    range: str = Field(...,example="<=24")
    gender: str = Field(...,example="F")
    amount: float = Field(...,example="345432.0")


class AccumulatedInfo(BaseModel):
    total: int
    ranges: List[RangeGender] = []


class Region(BaseModel):
    name: str
    geom: str


class PostalCode(BaseModel):
    id: int
    code: int
    geom: str
    total: int


class PostalCodesInfo(BaseModel):
    postalcodes: List = [PostalCode]


    
