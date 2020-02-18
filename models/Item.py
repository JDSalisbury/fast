from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    active: bool = True
    color: str = Field(None, title="The Color of the Item.", max_length=20)
