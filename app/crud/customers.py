from app.schemas.customers import CustomerCreate,CustomerUpdate
from app.models.customers import Customer
from sqlalchemy.orm import Session


def CreateCustomer(db:Session,customer:CustomerCreate):
    db_customer=Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def GetCustomer(db:Session,customerid:int):
    return db.query(Customer).filter(Customer.id==customerid).first()

def GetCustomers(db:Session,skip:int=0,limit:int=100):
    return db.query(Customer).offset(skip).limit(limit).all()

def DeleteCustomer(db:Session,customerid:int):
    db_customer=db.query(Customer).filter(Customer.id==customerid).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer

def UpdateCustomer(db:Session,customerid:int,customer:CustomerUpdate):
    db_customer=db.query(Customer).filter(Customer.id==customerid).first()
    if not db_customer:
        return None
    updated_data=customer.model_dump()
    for key,value in updated_data.items():
        setattr(db_customer,key,value)
    db.commit()
    db.refresh(db_customer)

    return db_customer
