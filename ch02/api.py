from fastapi import FastAPI
from ch02.todo import router
from ch02.inventory_route import inv_router

app = FastAPI(
    title= "Traincote Api",
    description= "This is Learning API"
)

app.include_router(router)
app.include_router(inv_router)