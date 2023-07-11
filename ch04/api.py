from fastapi import FastAPI
from ch04.todo import todo_router


app = FastAPI(
    title= "Traincote Api : CH04",
    description= "This is Learning API for chapter 4"
)

app.include_router(todo_router)