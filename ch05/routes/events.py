from fastapi import APIRouter, HTTPException, status, Body
from model.events import Event
from typing import List

event_router =  APIRouter(tags=["Events"])

events = [] # all events will be registered here.

@event_router.get('/', response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events

@event_router.get('/{id}', response_model=Event)
async def retrieve_single_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ID does not exist")

@event_router.post('/create')
async def create_new_event(event: Event = Body(...)) -> dict:
    events.append(event)
    return {
        "message": "Event created successfully"
    }

@event_router.delete('/delete')
async def delete_all_events():
    events.clear()
    return {
        "message": "Events delete successfully"
    }

@event_router.delete('/delete/{id}')
async def delete_single_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event deleted successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
        )