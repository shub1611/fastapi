from fastapi import APIRouter
from ch02.model import ToDo, TodoItem

router = APIRouter(tags=["ToDo"])

todo_list = []


@router.get("/hello")
async def say_hello():
    return {"message": "Hello World"}

@router.post("/create_todo")
async def create_todo(todo: ToDo) -> dict:
    todo_list.append(todo)
    return  {"message": "ToDo added successfully"}

# @router.post("/create_todo2")
# async def create_todo(todo: list) -> dict:
#     todo_list.append(todo)
#     return  {"message": "ToDo added successfully"}

@router.get("/get_todo")
async def fetch_todo():
    return {"todos": todo_list}

@router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied id doesn't exist"}

@router.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todo_data:TodoItem):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"todo": todo}
    return {"message": "Todo with supplied id doesn't exist"}

@router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return "Deleted successfully"
    return {"message": "Todo with supplied id doesn't exist"}