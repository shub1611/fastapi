from fastapi import APIRouter, HTTPException, status, Depends
from model.events import Event, EventUpdate
from typing import List
from database.connection import get_session
from sqlmodel import select

event_router =  APIRouter(tags=["Events"])

events = [] # all events will be registered here.

@event_router.get('/', response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    query = select(Event)
    events = session.exec(query).all()
    return events

@event_router.get('/{id}', response_model=Event)
async def retrieve_single_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ID does not exist")

@event_router.post('/create')
async def create_new_event(event: Event, session=Depends(get_session)) -> dict:
    session.add(event)
    session.commit()
    session.refresh(event)
    return {
        "message": "Event created successfully"
    }

@event_router.delete('/delete')
async def delete_all_events(session=Depends(get_session)):
    event = session.get(Event).all()
    if event:
        session.delete(event)
        session.commit()
        return {
            "message": "Events delete successfully"
        }

@event_router.delete('/delete/{id}')
async def delete_single_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {
            "message": "Events delete successfully"
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
        )

@event_router.put('/update/{id}')
async def update_event(id: int, new_event: EventUpdate, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        event_data = new_event.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ID does not exist")