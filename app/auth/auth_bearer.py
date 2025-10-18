from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from jose import jwt, JWTError
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM
from app.schemas.users import TokenData

security=HTTPBearer()

def current_user(token:HTTPAuthorizationCredentials=Depends(security))->TokenData:
    try:
        payload=jwt.decode(token.credentials,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        role:str=payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401,detail="username not found")
        return TokenData(username=username,role=role)
    except JWTError:
        raise HTTPException(status_code=401,detail="invalid token")
    

def require_role(required_role:str):
    def role_dependency(user:TokenData=Depends(current_user)):
        if user.role!=required_role:
            raise HTTPException(status_code=403,detail="you dont have access to this resourse")
        return user
    return role_dependency