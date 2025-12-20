# from pydantic import BaseModel,Field
# from typing import List


# class book(BaseModel):
#     book_id:int
#     book_name:str
#     book_des:str
#     author_id:int
#     cat_id:int

# class auth(BaseModel):
#     author_id:int=Field(...,examples=[1])
#     author_name:str=Field(...,examples=['George R. R. Martin'])
#     author_story:str=Field(...,examples=['(both auto and bio) or(auto)or (bio)' ])

# class category(BaseModel):
#     cat_name:str=Field(...,examples=['Coding'])
#     cat_des:str=Field(...,examples=['To grow your knowledge in coding'])

