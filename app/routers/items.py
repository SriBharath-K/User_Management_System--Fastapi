from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.schemas.items import ItemCreate, ItemOut,ItemUpdate
from app.crud import items
from app.db.database import get_db
from app.schemas.users import TokenData
from app.auth.auth_bearer import require_role

router=APIRouter(
    prefix="/app/items",
    tags=["item"]
)

@router.post("/creating_item",response_model=ItemOut)
def create_item(item:ItemCreate,db:Session=Depends(get_db),user: TokenData = Depends(require_role("admin"))):
    return items.CreateItem(db,item)

@router.get("/get_item/{itemid}",response_model=ItemOut)
def get_item(itemid:int,db:Session=Depends(get_db)):
    return items.GetItem(db,itemid)

@router.get("/get_items/",response_model=list[ItemOut])
def get_items(skip:int,limit:int,db:Session=Depends(get_db)):
    return items.GetItems(db,skip,limit)

@router.delete("/delete_item/{itemid}",response_model=ItemOut)
def delete_item(itemid:int,db:Session=Depends(get_db),user: TokenData = Depends(require_role("admin"))):
    return items.DeleteItem(db,itemid)

@router.put("/update_item/{itemid}",response_model=ItemOut)
def item_update(itemid:int,item:ItemUpdate,db:Session=Depends(get_db),user: TokenData = Depends(require_role("admin"))):
    return items.UpdateItem(db,itemid,item)


