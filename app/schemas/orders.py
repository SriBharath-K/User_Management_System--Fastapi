from pydantic import BaseModel
from typing import Optional,List

class orderCreate(BaseModel):
    name: str
    quantity: int

class orderUpdate(BaseModel):
    name: Optional[str]=None
    quantity: Optional[int]=None

class orderOut(BaseModel):
    id: int
    name:str
    quantity:int

    class Config:
        from_attributes  = True 