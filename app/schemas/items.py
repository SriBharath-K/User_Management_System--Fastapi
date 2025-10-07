from pydantic import BaseModel
from typing import Optional,List

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int

class ItemUpdate(BaseModel):
    name: Optional[str]=None
    description: Optional[str] = None
    price: Optional[int]=None

class ItemOut(BaseModel):
    id: int
    name:str
    description:Optional[str]=None
    price:int

    class Config:
        from_attributes  = True 