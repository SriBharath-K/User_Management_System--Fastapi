from sqlalchemy.orm import Session
from app.models.orders import Orders
from app.schemas.orders import orderCreate,orderUpdate
from fastapi import HTTPException

def CreateOrder(db:Session,order:orderCreate):
    db_order=Orders(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def GetOrder(db:Session,orderid:int):
    db_order=db.query(Orders).filter(orderid==Orders.id).first()
    if not db_order:
        raise HTTPException(status_code=404,detail="order not found")
    return db_order

def GetOrders(db:Session,skip:int,limit:int):
    return db.query(Orders).all()

def DeleteOrder(db:Session,orderid:int):
    db_order=db.query(Orders).filter(orderid==Orders.id).first()
    if not db_order:
        raise HTTPException(status_code=404,detail="order not found")
    db.delete(db_order)
    db.commit()
    return db_order

def UpdateOrder(db:Session,orderid:int,order:orderUpdate):
    db_order=db.query(Orders).filter(orderid==Orders.id).first()
    if not db_order:
        raise HTTPException(status_code=404,detail="order not found")
    updated_order=order.model_dump(exclude_unset=True)
    for key,value in updated_order.items():
        setattr(db_order,key,value)
    db.commit()
    db.refresh(db_order)
    return db_order