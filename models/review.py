from pydantic import BaseModel, Field, validator


class review(BaseModel):
    review_id: int = Field(..., examples=[1])
    rating: int = Field(..., examples=[4])
    title: str = Field(..., examples=['Good and inspiring story'])
    content: str = Field(..., examples=['Very engaging and motivating book'])

    @validator('review_id')
    def validator_review_id(cls, review_id):
        if review_id == 0:
            raise ValueError('fill the id')
        return review_id

    @validator('rating')
    def validator_rating(cls, rating):
        if rating < 1 or rating > 5:
            raise ValueError('rating must be between 1 and 5')
        return rating

    @validator('title')
    def validator_title(cls, title):
        if title.strip() == '' or title == 'string':
            raise ValueError('fill the title')
        return title

    @validator('content')
    def validator_content(cls, content):
        if content.strip() == '' or content == 'string':
            raise ValueError('fill the content')
        return content


class updates(BaseModel):
    title: str = Field(..., examples=['Updated review title'])
    content: str = Field(..., examples=['Updated review content'])

    @validator('title')
    def validator_title(cls, title):
        if title.strip() == '' or title == 'string':
            raise ValueError('fill the title')
        return title

    @validator('content')
    def validator_content(cls, content):
        if content.strip() == '' or content == 'string':
            raise ValueError('fill the content')
        return content
