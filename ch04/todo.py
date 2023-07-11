from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

todo_router = APIRouter(tags=["ToDo-HTML"])
todo_list = []

template = Jinja2Templates(directory='./ch04/templates')

@todo_router.post('/todo')
async def add_todo(request: Request):
    pass


@todo_router.get('/todo')
async def get_todo(request: Request):
    return template.TemplateResponse('todo.html', {'request': request, 'todos': todo_list})