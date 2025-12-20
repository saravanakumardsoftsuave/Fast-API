from fastapi import APIRouter,Depends,HTTPException,status,Response
from models.books_service import books,update
from utils.database import get_database
from service.book_service import book_service



book_route=APIRouter(prefix='/books',tags=['list_of_Books'])

@book_route.post('/')
async def create_book(bookss:books,db=Depends(get_database)):
    res=book_service(db)
    result = await res.create_one(bookss)
    if not result:
        raise HTTPException(status_code=409, detail="Book already exists")
    return result
 
@book_route.get('/one')
async def retr_one(book_id:int,db=Depends(get_database)):
    res=book_service(db)
    result=await res.retr_one(book_id)
    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result

@book_route.get('/all')
async def ret_all(limit:int,page:int,db=Depends(get_database)):
    res=book_service(db)
    result=await res.retireve_all(limit,page)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result

@book_route.put('/update')
async def update(book_id:int,update:update,db=Depends(get_database)):
    res=book_service(db)
    book= await res.update(book_id,update)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return book
@book_route.delete('/delete/{book_id}')
async def delete_on(book_id:int,db=Depends(get_database)):
    res=book_service(db)
    book=await res.del_user(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return book
