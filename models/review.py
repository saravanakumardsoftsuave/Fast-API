from pydantic import BaseModel

class review(BaseModel):
    review_id:int
    rating:int
    title:str
    content:str


class updates(BaseModel):
    title:str
    content:str
    