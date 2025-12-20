from pydantic import BaseModel,Field,validator
from typing import List

from models.books_service import books

class authors(BaseModel):
    author_id:int=Field(...,examples=[1])
    author_name:str=Field(...,examples=['George R. R. Martin'])
    author_story:str=Field(...,examples=['(both auto and bio) or(auto)or (bio)' ])

class update_author(BaseModel):
    author_name:str=Field(...,examples=['J.K. Rowling'])
    author_story:str=Field(...,examples=['A Game of Thrones'])
    @validator('author_name')
    def validator_author_name(cls,author_name):
        if author_name.strip()=='' or author_name == 'string':
            raise ValueError('fill the correct name')
        return author_name
    @validator('author_story')
    def validator_author_story(cls,author_story):
        if author_story.strip()=='' or author_story == 'string':
            raise ValueError('fill the valid one')
        return author_story
class book_and_author(BaseModel):
    author_id:int=Field(...,examples=[1])
    author_name:str=Field(...,examples=['George R. R. Martin'])
    author_story:str=Field(...,examples=['(both auto and bio) or(auto)or (bio)' ])
    book:List[books]