from pydantic import BaseModel,Field,EmailStr,validator

class users(BaseModel):
    user_id:int
    name:str=Field(...,examples=['saran'])
    email:EmailStr=Field(...,examples=['selva@gmail.com'])
    password:str=Field(...,examples=['selva@12'])
    review_count:int=0
    @validator('email')
    def validation(cls,email):
        if email!=email.lower() or  not email.endswith('@gmail.com'):
            raise ValueError('Not a valid email')
        else:
            return email
class updates(BaseModel):
    name:str
    email:EmailStr
    password:str
    @validator('email')
    def validation(cls,email):
        if email!=email.lower() or  not email.endswith('@gmail.com'):
            raise ValueError('Not a valid email')
        else:
            return email
    @validator('name')
    def validators(cls,name):
        if name.strip()=='' or name == 'string':
            raise ValueError('fill the name ')
        return name
    @validator('password')
    def validator_pas(cls,password):
        if password.strip()=='' or password == 'string':
            raise ValueError('fill the password ')
        return password