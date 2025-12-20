from pydantic import BaseModel,Field,validator

class category(BaseModel):
    cat_id : int=(Field(...,examples=[1]))
    cat_name:str=Field(...,examples=['Anime'])
    cat_des:str=Field(...,examples=['To entertainment and motivations'])

class update_one(BaseModel):
    cat_name:str=Field(...,examples=['Coding'])
    cat_des:str=Field(...,examples=['To grow your knowledge in coding'])
    @validator('cat_name')
    def validators_name(cls,cat_name):
        if cat_name.strip()=='' or cat_name == 'string':
            raise ValueError('fill the name ')
        return cat_name
    @validator('cat_des')
    def validator_des(cls,cat_des):
        if cat_des.strip()=='' or cat_des == 'string':
            raise ValueError('fill the name ')
        return cat_des