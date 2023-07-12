from typing import List, Optional
from sqlmodel import SQLModel, Field, Column, JSON


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

class EventUpdate(SQLModel):
    title: Optional[str] 
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]
