from fastapi import APIRouter, HTTPException, status
from ch03.model import TodoItems

todo_router = APIRouter(tags=["ToDo"])
todo_list = [
    {"id":1, "item":"1"},
    {"id":2, "item":"2"},
    {"id":3, "item":"3"}
             ]

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo():
    return {"todos":todo_list}

@todo_router.get("/todo/{id}", status_code=201)
async def get_one(id: int):
    for todo  in todo_list:
        if todo.get("id") == id:
            return {"todo" : todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="ID not found")