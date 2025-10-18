from pydantic import EmailStr,BaseModel,Field
from typing import Annotated,Optional

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    role:str
    password:str

class UserLogin(BaseModel):
    username:str
    password:str

class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    role:str
    model_config = {"from_attributes": True}

class TokenData(BaseModel):
    username:str
    role:str


