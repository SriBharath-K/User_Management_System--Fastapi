from ..db.database import BASE
from sqlalchemy import Column,Integer,String

class Items(BASE):
    __tablename__="items"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String,nullable=True)
    price=Column(Integer,nullable=False)