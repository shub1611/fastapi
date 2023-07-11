from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

todo_router = APIRouter(tags=["ToDo-HTML"])
todo_list = [{"title": 1}, {"title":2}]

template = Jinja2Templates(directory='./ch04/templates')

@todo_router.post('/todo')
async def add_todo(request: Request):
    pass

@todo_router.get('/todo')
async def get_todo(request: Request):
    return template.TemplateResponse('todo.html', {'request': request, 'todos': todo_list})

@todo_router.get('/todo-create')
async def get_todo(request: Request):
    return template.TemplateResponse('todo_form.html', {'request': request})

@todo_router.post("/todo-save")
async def save(request: Request, item: str = Form(...)):
    print('item =', item)
    todo_list.append({"title": item})
    return 'ok'