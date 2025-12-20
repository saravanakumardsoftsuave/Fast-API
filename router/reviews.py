from fastapi import APIRouter,Depends,status,HTTPException
from service.review_service import review_ser
from utils.database import get_database
from models.review import review,updates

review_route=APIRouter(prefix='/review',tags=['Review'])


@review_route.post('/',status_code=status.HTTP_201_CREATED)

async def create(review:review,book_id:int,user_id:int,db=Depends(get_database)):
    res=review_ser(db)
    result=await res.create_one(review,book_id,user_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='Already exists')
    return result

@review_route.get('/one/{book_id}/review/{review_id}')
async def retr(book_id:int,review_id:int,db=Depends(get_database)):
    res=review_ser(db)
    result= await res.retr_one(book_id,review_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result

@review_route.get('/update/{review_id}')
async def updating(review_id:int,update:updates,db=Depends(get_database)):
    res=review_ser(db)
    result= await res.update(review_id,update)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return result