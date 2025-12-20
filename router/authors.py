from fastapi import APIRouter,Depends
from models.authors_books import authors,update_author,book_and_author
from utils.database import get_database
from service.authors_ser import authors_cls
from fastapi import HTTPException,status
authors_route=APIRouter(prefix='/authors', tags=['authors'])

@authors_route.post('',status_code=status.HTTP_201_CREATED)
async def create_one(auth_book:authors,db=Depends(get_database)):
    res=authors_cls(db)
    auth=await res.create_one(auth_book)
    if not auth:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='The author_id already exists')
    return auth

@authors_route.get('/',status_code=status.HTTP_200_OK)
async def retireve_all(limit:int,page:int,db=Depends(get_database)):
    res=authors_cls(db)
    result=await res.retr_all(limit,page)
    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result

@authors_route.get('/one', response_model=book_and_author,status_code=status.HTTP_200_OK)
async def get_one(author_id:int,db=Depends(get_database)):
    res=authors_cls(db)
    result=await res.retr_one(author_id)
    if not res:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data founded')
    return result

@authors_route.put('/',status_code=status.HTTP_200_OK)
async def update_book_and_author(author_name:str,update:update_author,db=Depends(get_database)):
    res=authors_cls(db)
    result=await res.updating(author_name,update)
    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result

@authors_route.delete('/',status_code=status.HTTP_200_OK)
async def delete(author_name:str,db=Depends(get_database)):
    res=authors_cls(db)
    result=await res.deleting(author_name)
    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result