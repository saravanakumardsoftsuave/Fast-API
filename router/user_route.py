from fastapi import APIRouter,Depends
from utils.database import  get_database
from models.user_login import users,updates
from models.user_login_page import login
from service.security import token,get_current
from service.user_service import user_class
from fastapi import HTTPException,status
user_route=APIRouter(prefix='/user',tags=['Users'])

@user_route.post('/',status_code=status.HTTP_201_CREATED)
async def create_user(user:users,db=Depends(get_database)):
    service=user_class(db)
    result=await service.user_create (user)
    if not result:
        raise HTTPException(status_code=409,detail='Email already exists')
    else:
        return result
@user_route.post('/login')
async def login(gmail:str,password:str,db=Depends(get_database)):
    res=user_class(db)
    user=await res.login(gmail,password)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    tok=token(data={'sub':user['user_id']})
    tok_days=token(data={'sub':user['user_id']})
    return{
        'day_tok':tok_days,
        'token':tok,
        'message':'login successfull'
    }

@user_route.get('/current_user')
async def current_user(token: str, db=Depends(get_database)):
    current_user = await get_current(token, db)
    return {
        'user_id': str(current_user['_id']),
        'name': current_user['name'],
        'email': current_user['email']
    }

@user_route.get('/',status_code=status.HTTP_200_OK)
async def retireve_user(limit:int,page:int,db=Depends(get_database)):
    result=user_class(db)
    user= await result.user_retireve(limit,page)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return user

@user_route.get('/one',status_code=status.HTTP_302_FOUND)
async def one_retireve(email:str,db=Depends(get_database)):
    res=user_class(db)
    user=await res.user_ret(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return user

@user_route.put('/update')
async def update_data(email:str,update:updates,db=Depends(get_database)):
    res=user_class(db)
    user=await res.update_user(email,update)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return user


@user_route.delete('/delete')
async def delete_on(email:str,db=Depends(get_database)):
    res=user_class(db)
    user=await res.del_user(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return user