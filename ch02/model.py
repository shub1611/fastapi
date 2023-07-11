from pydantic import BaseModel

class TodoItem(BaseModel):
    item: str

class ToDo(BaseModel):
    id: int
    item: TodoItem