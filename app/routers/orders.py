from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.schemas.orders import orderCreate, orderOut,orderUpdate
from app.crud import orders
from app.db.database import get_db

router=APIRouter(
    prefix="/app/orders",
    tags=["orders"]
)

@router.post("/create",response_model=orderOut)
def createorder(order:orderCreate,db:Session=Depends(get_db)):
    return orders.CreateOrder(db,order)

@router.get("/get_order/{orderid}",response_model=orderOut)
def getorder(orderid:int,db:Session=Depends(get_db)):
    return orders.GetOrder(db,orderid)

@router.get("/get_orders/",response_model=list[orderOut])
def getorders(skip:int,limit:int,db:Session=Depends(get_db)):
    return orders.GetOrders(db,skip,limit)

@router.delete("/delete/{orderid}",response_model=orderOut)
def deleteorder(orderid:int,db:Session=Depends(get_db)):
    return orders.DeleteOrder(db,orderid)

@router.put("/update/{orderid}",response_model=orderOut)
def updateorder(orderid:int,order:orderUpdate,db:Session=Depends(get_db)):
    return orders.UpdateOrder(db,orderid,order)