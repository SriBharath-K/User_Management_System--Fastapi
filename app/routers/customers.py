from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.schemas.customers import CustomerCreate, CustomerOut,CustomerUpdate
from app.crud import customers
from app.db.database import get_db
from app.auth.auth_bearer import current_user
from app.schemas.users import TokenData
from app.auth.auth_bearer import require_role

router=APIRouter(
    prefix="/app/Customers",
    tags=["customer"]
)
@router.post("/creating_customer", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db),user: TokenData = Depends(require_role("admin"))):
    return customers.CreateCustomer(db, customer)

@router.get("/get_customer/{customerid}",response_model=CustomerOut)
def get_customer(customerid:int,db:Session=Depends(get_db)):
    db_customer= customers.GetCustomer(db,customerid)
    if not db_customer:
        raise HTTPException(status_code=404,detail="customer not found")
    return db_customer

@router.get("/get_customers",response_model=list[CustomerOut])
def get_customers(skip,limit,db:Session=Depends(get_db)):
    return customers.GetCustomers(db,skip,limit)

@router.delete("/delete_customer/{customerid}",response_model=CustomerOut)
def delete_customer(customerid:int,db:Session=Depends(get_db),user: TokenData = Depends(require_role("admin"))):
    db_customer= customers.DeleteCustomer(db,customerid)
    if not db_customer:
        raise HTTPException(status_code=404,detail="customer not found")
    return db_customer

@router.put("/update_customer/{customerid}",response_model=CustomerOut)
def update_customer(customerid:int,customer:CustomerUpdate,db:Session=Depends(get_db),user: TokenData = Depends(require_role("admin"))):
    db_customer=customers.UpdateCustomer(db,customerid,customer)
    if not db_customer:
        raise HTTPException(status_code=404,detail="customer not found")
    return db_customer