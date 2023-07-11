from fastapi import FastAPI
from ch03.todo import todo_router
from ch03.inv_router import inv_router

app = FastAPI(
    title= "Traincote Api : CH03",
    description= "This is Learning API for chapter 3"
)

app.include_router(todo_router)
app.include_router(inv_router)
