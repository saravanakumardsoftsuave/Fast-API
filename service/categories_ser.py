from fastapi import HTTPException,status
class categiores:
    def __init__(self,db):
        self.collection=db['categories1']

    async def create_cat(self,new):
        exits=await self.collection.find_one({'cat_name':new.cat_name})
        if exits:
            return None
        user=await self.collection.insert_one({
            'cat_id':new.cat_id,
            'cat_name':new.cat_name,
            'cat_des':new.cat_des
        })
        return {
            'cat_id':new.cat_id,
            'message':'success'
        }
    
    async def retr_all(self,limit,page):
        total = await self.collection.count_documents({})
        skip=(page-1)*limit
        if skip<=total or total==0:
            cat=self.collection.find().skip(skip).limit(limit)
            if not cat:
                return None
            res=[]
            async for cats in cat:
                cats['_id']=str(cats['_id'])
                res.append(cats)
            return res
        else:
             raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Page number out of range"
    )   


    async def retr_one(self,cat_name):
        res=await self.collection.find_one({'cat_name':cat_name})
        if not res:
            return None
        res['_id']=str(res['_id'])
        return res


    async def update(self,cat_name,update):
        cat = await self.collection.find_one({'cat_name':cat_name})
        if not cat:
            return None
        res=await self.collection.update_one({'cat_name':cat_name},
                                        {"$set":update.dict()})
        return {
            'message':'updated',
            'cat_id':str(cat['_id'])
        }

    async def delete(self,cat_name):
        if not await self.collection.find_one({'cat_name':cat_name}):
            return None
        await self.collection.delete_one({
            'cat_name':cat_name
        })
        return {
            'message':'Deleted Successfully'
        }
        