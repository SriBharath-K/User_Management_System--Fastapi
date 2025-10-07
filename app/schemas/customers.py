from pydantic import BaseModel,EmailStr
from typing import Optional,List

class CustomerCreate(BaseModel):
    name:str
    email: EmailStr

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class CustomerOut(BaseModel):
    id:int
    name:str
    email:EmailStr

    class Config:
        from_attributes  = True 
    