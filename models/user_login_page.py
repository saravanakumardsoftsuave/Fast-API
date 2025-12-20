from pydantic import BaseModel,Field

class login(BaseModel):
    gamil:str
    password:str


class token(BaseModel):
    access_token:str
    token_type:str='bearer'