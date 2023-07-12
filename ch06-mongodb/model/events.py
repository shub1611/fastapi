from typing import List, Optional
from pydantic import BaseModel
from beanie import Document


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        # this will map to collection name
        name = "events"

class EventUpdate(BaseModel):
    title: Optional[str] 
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]
