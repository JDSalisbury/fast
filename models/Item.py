from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set


# Set is used for a list of unique items. good for tags.


class Image(BaseModel):
    url: HttpUrl
    name: str
    default: str


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    active: bool = True
    color: str = Field(None, title="The Color of the Item.", max_length=20)
    tags: Set[str] = set()
    comments: List[str] = []
    image: Image = None
    images: Set[Image] = set()
