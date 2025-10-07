from pydantic import EmailStr,BaseModel,Field
from typing import Annotated

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    username:str
    password:str

class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    model_config = {"from_attributes": True}