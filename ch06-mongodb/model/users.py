from pydantic import BaseModel, EmailStr
from typing import List, Optional
from model.events import Event
from beanie import Document, Link

# this is to register a user
class User(Document):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Link[Event]]] = None
    class Settings:
        name = "users"


# this class will be used to log-in into app
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
