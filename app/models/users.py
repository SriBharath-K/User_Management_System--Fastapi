from sqlalchemy import Column,Integer,String
from app.db.database import BASE

class User(BASE):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(255),unique=True,index=True)
    role = Column(String(20), default="user")
    email=Column(String(255),unique=True,index=True)
    hashed_password=Column(String(255))