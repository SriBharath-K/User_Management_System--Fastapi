from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine,BASE
from app.models.customers import Customer
from app import models
from app import routers
from app.routers.customers import router as customer_router
from app.routers.items import router as item_router
from app.routers.orders import router as order_router
from app.routers.users import router as user_router
from app.auth.auth_bearer import current_user


# Create database tables
BASE.metadata.create_all(bind=engine)

app = FastAPI(
    title="customer API"
)
app.include_router(customer_router)
app.include_router(item_router)
app.include_router(order_router)
app.include_router(user_router)




@app.get("/login")
def home(username:str=Depends(current_user)):
    return {"message": "Welcome to fastapi Customer App!"}


