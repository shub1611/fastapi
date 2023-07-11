from pydantic import BaseModel
from typing import List

class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "example" : {
                "item": "The item name, eg: bag"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        json_schema_extra = {
            "example": {
                "todos" : [
                    {"item": "Example1"},
                    {"item": "Example2"}
                ]
            }
        }

class Items(BaseModel):
    name: str
    price: float