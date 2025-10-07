from ..db.database import BASE
from sqlalchemy import Column,Integer,String



class Customer(BASE):
    __tablename__="customers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,unique=True)
