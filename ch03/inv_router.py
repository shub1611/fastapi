from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import APIRouter, HTTPException, status
from ch03.model import Items

inv_router = APIRouter(tags=["Inventory"], prefix="/inv")
"""
1: create engine
2: session
3: generate table using declarative_base from model
4: execute
"""

db_url = "sqlite:///./ch03/inventory.db"
engine = create_engine(db_url, connect_args={"check_same_thread": False})

session = sessionmaker(bind=engine)
db = session()

# get a parent of all models
Base = declarative_base()
class Item(Base):
    __tablename__ =  'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)

#Below command will create the table (if not available)
Base.metadata.create_all(engine)

# Insert a data
# item = Item(name='Shoes', price=99.99)
# db.add(item) # insert into item (name, price) values('Shoes',99.99)


# list all inventory
@inv_router.get("/")
async def get_all_inv():
    # query data
    rows = db.query(Item).all()
    db.close()
    # for row in rows:
    #     print(row.id, row.name, row.price)
    return rows

@inv_router.get("/{id}")
async def get_single_inv(id: int):
    # query data
    # row = db.query(Item).get({"id":id})
    row = db.query(Item).filter(Item.id == id).first()
    db.close()
    # for row in rows:
    #     print(row.id, row.name, row.price)
    return row

@inv_router.post("/create")
async def create_inv(item: Items):
    items = Item(**item.model_dump())
    row = db.add(items)
    db.commit()
    db.refresh(items)
    db.close()
    return items

@inv_router.put("/update/{id}")
async def update_inv(id:int, item: Items):
    db_item = db.query(Item).filter(Item.id == id).first()
    db_item.name = item.name
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item


@inv_router.delete("/delete/{id}")
async def delete_inv(id:int):
    db_item = db.query(Item).filter(Item.id == id).first()
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")
    db.delete(db_item)
    db.commit()
    db.close()
    return {"message": "delete ok"}