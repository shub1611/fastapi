from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from routes.users import user_router
from routes.events import event_router
from database.connection import Settings

app = FastAPI(
    title= "Traincote Api : CH06-MongoDb",
    description= "FastAPI SQLModel learning in chapter 6"
)


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/events")

setting = Settings()

# this will open connection to DB and create tables
@app.on_event("startup")
async def on_startup():
    await setting.initialize_database()


# @app.get("/")
# async def home():
#     return RedirectResponse(url='/event')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)