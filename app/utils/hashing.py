from passlib.context import  CryptContext

pwd_context=CryptContext(schemes=["argon2"],deprecated="auto")

#hashing befor saving into db(during signup)
def hash_password(password:str):
    return pwd_context.hash(password)

#verify before login(during Login)
def verify_password(plainpassword,hashpassword):
    return pwd_context.verify(plainpassword,hashpassword)
