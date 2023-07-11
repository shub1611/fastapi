from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

inv_router =  APIRouter()
path = "C:\\Users\\TMY-01\\Desktop\\FastAPI\\code\\ch02\\inventory.db"
conn = sqlite3.connect(path)
curr = conn.cursor()

class Item(BaseModel):
    name: str
    price: float

@inv_router.get("/inv")
async def get_all_inv():
    query = "select * from items"
    items = curr.execute(query)
    return list(items)
    
@inv_router.get("/inv/{id}")
async def get_all_inv(id):
    query = "select * from items where id=" + str(id)
    item = curr.execute(query)
    return list(item)

@inv_router.post("/inv")
async def create_inv(item:Item):
    query = "INSERT INTO items(name, price) VALUES(?,?)"
    item = curr.execute(query, [item.name, item.price])
    conn.commit()
    return {"message": "ok"}
