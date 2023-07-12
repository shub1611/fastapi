from fastapi import APIRouter, HTTPException, status, Depends
from model.events import Event, EventUpdate
from typing import List
from beanie import PydanticObjectId
from database.connection import Database

event_router = APIRouter(tags=["Events"])
event_database =  Database(Event)


@event_router.get('/', response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get('/{id}', response_model=Event)
async def retrieve_single_event(id: str) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID does not exist")
    return event

@event_router.post('/create')
async def create_new_event(event: Event) -> dict:
    await event_database.save(event)
    return {
        "message": "Event created successfully"
    }

# @event_router.delete('/delete')
# async def delete_all_events(session=Depends(get_session)):
#     event = session.get(Event).all()
#     if event:
#         session.delete(event)
#         session.commit()
#         return {
#             "message": "Events delete successfully"
#         }

@event_router.delete('/delete/{id}')
async def delete_single_event(id: str, ) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
            )
    return {
        "message": "Event deleted successfully"
    }

@event_router.put('/update/{id}')
async def update_event(id: PydanticObjectId, new_event: EventUpdate) -> Event:
    event = await event_database.update(id, new_event)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID does not exist")
    return event