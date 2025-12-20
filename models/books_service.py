from pydantic import BaseModel,Field,validator
from typing import List
class books(BaseModel):
    book_id:int
    book_name:str
    book_des:str
    author_id:int
    cat_id:int

class update(BaseModel):
    book_name:str
    book_des:str
    @validator('book_name')
    def validators(cls,book_name):
        if book_name.strip()=='' or book_name == 'string':
            raise ValueError('fill the name ')
        return book_name
    @validator('book_des')
    def validator_des(cls,book_des):
        if book_des.strip()=='' or book_des == 'string':
            raise ValueError('fill the name ')
        return book_des
# class bookall(BaseModel):
#     book_id:int
#     book_name:str
#     book_des:str
#     author:List[authors]
#     cat:List[category]