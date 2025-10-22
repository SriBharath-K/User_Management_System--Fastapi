from ..db.database import BASE
from sqlalchemy import Column,Integer,String

class Orders(BASE):
    __tablename__="orders"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(255),nullable=False)
    quantity=Column(Integer,nullable=False)