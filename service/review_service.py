from fastapi import HTTPException,status
class review_ser:
    def __init__(self,db):
        self.collection=db['reviews']
        self.users=db['user_create']
        self.book=db['books']
    # async def retr_one(self,book_id):
    #     pipeline=[
    #         {'$match':{'book_id':book_id}},
    #         # {
    #         #     '$lookup':{
    #         #         'from':'reviews',
    #         #         'localField':'book_id',
    #         #         'foreignField':'book_id',
    #         #         'as':'reviews'
    #         #     }
    #         # },
    #         {
    #             '$lookup':
    #             {
    #                 'from':'users_create',
    #                 'localField':'user_id',
    #                 'foreignField':'user_id',
    #                 'as':'user_create'
    #             }
    #         },
    #         {
    #             '$project':{
    #                 '_id':0,
    #                 # 'reviews._id':0,
    #                 'user_create._id':0
    #             }
    #         }
    #     ]
    #     return await self.collection.aggregate(pipeline).to_list(None)
    
    async def create_one(self,review,book_id,user_id):
        book = await self.book.find_one({ 'book_id' : book_id })
        if not book:
            return None
        user = await self.users.find_one({ 'user_id' : user_id})
        if not user:
            return None

        review_dict = review.dict()
        review_dict['book_id'] = book_id
        review_dict['user_id'] = user_id
        await self.collection.insert_one(review_dict)
        return{
            'message':'created'
        }
    
    async def retr_one(self,book_id,review_id):
        res = await self.collection.find_one({
        'book_id': book_id,
        'review_id': review_id})
        if not res:
            return None
        res['_id']=str(res['_id'])
        user = await self.users.find_one(
            {'user_id': res['user_id']},
            {'_id': 0,'user_id':1,'name':1} 
        )

        if user:
            res['user'] = user
        return res
    async def update(self,review_id,update):
        res=await self.collection.find_one({'review_id':review_id}).to_list(lenght=None)
        if not res:
            return  None
        result=await self.collection.update_one({"review_id":review_id},
                                                {'$set':update})
        return result