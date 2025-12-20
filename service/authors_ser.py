from fastapi import HTTPException,status
class authors_cls:
    def __init__(self,db):
        self.collection=db['Authors_Books']
        self.book=db['books']
    async def create_one(self,auth_book):
        exists=await self.collection.find_one({'author_id':auth_book.author_id})
        if exists:
            return None
        await self.collection.insert_one({
            'author_id':auth_book.author_id,
            'author_name':auth_book.author_name,
            'author_story':auth_book.author_story
        })
        return {
            'author_id':auth_book.author_id,
            'message':'Created'
        }

    async def retr_all(self,limit,page):
        t=await self.collection.count_documents({})
        skip=(page-1)*limit
        if  t>=skip or t==0:
            res= await self.collection.find().skip(skip).limit(limit).to_list(length=None)
            auth_bo=[]
            for r in res:
                r['_id']=str(r['_id'])
                auth_bo.append(r)
            return res
        else:
             raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Page number out of range"
    )   
         
    async def retr_one(self,author_id):
        res=await self.collection.find_one({'author_id':author_id})
        if not res:
            return None
        res['_id']=str(res["_id"])
        book=await self.book.find({'author_id':author_id}).to_list(length=None)
        book1=[]
        for b in book:
            b['_id']=str(b['_id'])
            book1.append(b)
        return {
        "author_id": res["author_id"],
        "author_name": res["author_name"],
        "author_story": res["author_story"],
        "book": book
    }
    async def updating(self,author_name,update):
        res= await self.collection.update_one({'author_name':author_name},
                                              {'$set':update.dict()})
        if not res:
           return None
        return {
            'message':'updated'
        }

    async def deleting(self,author_name):
        res=await self.collection.find_one({'author_name':author_name})
        if not res:
            return None
        await self.collection.delete_one({'author_name':author_name})
        return{'message':'deleted'}