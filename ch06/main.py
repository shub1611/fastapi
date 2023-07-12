from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from routes.users import user_router
from routes.events import event_router
from database.connection import conn

app = FastAPI(
    title= "Traincote Api : CH05",
    description= "This is Learning API for chapter 5"
)


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/events")

# this will open connection to DB and create tables
@app.on_event("startup")
def on_startup():
    conn()

# 
# @app.get("/")
# async def home():
#     return RedirectResponse(url='/event')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)