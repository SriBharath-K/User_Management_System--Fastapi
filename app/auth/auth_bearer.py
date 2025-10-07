from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from jose import jwt, JWTError
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM

security=HTTPBearer()

def current_user(token:HTTPAuthorizationCredentials=Depends(security)):
    try:
        payload=jwt.decode(token.credentials,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if not username:
            raise HTTPException(status_code=401,detail="username not found")
        return username
    except JWTError:
        raise HTTPException(status_code=401,detail="invalid token")