from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import timedelta,datetime,timezone
from utils.database import get_database
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status

oauth2 = OAuth2PasswordBearer(tokenUrl="/user/login")

SCERET_KEY='super-sceret-key'
ALOGRITHM='HS256'
ACCESS_TIME=1440 
REFRESH_TOKEN_EXPIRE_DAYS = 1

async def get_current(token: str, db=Depends(get_database)):
    try:
        payload = jwt.decode(token,SCERET_KEY, algorithms=[ALOGRITHM])
        user_id = payload.get('sub')
        if not user_id:
            raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid token')
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token expired'
        )
    
    user = await db['user_create'].find_one({'user_id': int(user_id)})
    if not user:
        raise credentials_exception
    
    return user

def token(data:dict):
    encode_=data.copy()
    exp = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TIME)  
    encode_.update({'exp':exp})
    return jwt.encode(encode_,SCERET_KEY,algorithm=ALOGRITHM)
def refresh_tok(data:dict):
    encode=data.copy()
    exp=datetime.now()+timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    encode.update({'exp':exp})
    return jwt.encode(encode,SCERET_KEY,algorithm=ALOGRITHM)
pwt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

@staticmethod
def verify_password(password:str,hashpassword:str):
    return pwt_context.verify(password,hashpassword)

@staticmethod
def hash_password(password:str):
    return pwt_context.hash(password)