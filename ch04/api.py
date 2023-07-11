from fastapi import FastAPI
from ch04.todo import todo_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title= "Traincote Api : CH04",
    description= "This is Learning API for chapter 4"
)

app.mount('/static', StaticFiles(directory='./ch04/static'), name='static')
app.include_router(todo_router)