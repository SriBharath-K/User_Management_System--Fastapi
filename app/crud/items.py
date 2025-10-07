from sqlalchemy.orm import Session
from app.models.items import Items
from app.schemas.items import ItemCreate,ItemUpdate


def CreateItem(db:Session,item:ItemCreate):
    db_item=Items(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def GetItem(db:Session,itemid:int):
    return db.query(Items).filter(itemid==Items.id).first()

def GetItems(db:Session,skip:int,limit:int):
    return db.query(Items).all()

def DeleteItem(db:Session,itemid:int):
    db_item=db.query(Items).filter(itemid==Items.id).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

def UpdateItem(db:Session, itemid: int, item: ItemUpdate):
    db_item = db.query(Items).filter(Items.id == itemid).first()
    if not db_item:
        return None
    update_data = item.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item