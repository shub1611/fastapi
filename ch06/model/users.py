from pydantic import BaseModel, EmailStr
from typing import List, Optional
from model.events import Event

# this is to register a user
class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = None


# this class will be used to log-in into app
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
