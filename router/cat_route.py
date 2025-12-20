from fastapi import APIRouter, Depends,HTTPException,status,Response
from models.categories import category,update_one
from utils.database import get_database
from service.categories_ser import categiores
cat_router=APIRouter(prefix='/categories',tags=['Categories'])

@cat_router.post('/')
async def cat_create(new:category,db=Depends(get_database)):
    res=categiores(db)
    cat=await res.create_cat(new)
    if not cat:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='Already exists')
    return cat

@cat_router.get('/all')
async def get_all(limit:int,page:int,db=Depends(get_database)):
    res=categiores(db)
    cat=await res.retr_all(limit,page)
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return cat

@cat_router.get('/getone/{cat_name}')
async def get_one(cat_name:str,db=Depends(get_database)):
    res=categiores(db)
    cat=await res.retr_one(cat_name)
    if not cat:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return cat

@cat_router.put('/{cat_name}')
async def update_cat(cat_name:str,update:update_one,db=Depends(get_database)):
    res=categiores(db)
    cat= await res.update(cat_name,update)
    if not cat:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return cat


@cat_router.delete('/delete/{cat_name}')
async def delete_cat(cat_name:str,db=Depends(get_database)):
    res=categiores(db)
    cat=await res.delete(cat_name)
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No data Founded')
    return cat