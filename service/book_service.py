from fastapi import HTTPException,status
class book_service:
    def __init__(self,db):
        self.collection=db['books']
        self.author=db['Authors_Books']
        self.cat=db['categories1']

    async def create_one(self,bookss):
        res=await self.collection.find_one({'book_name':bookss.book_name})
        if res:
            return None
        await self.collection.insert_one({
            'book_id':bookss.book_id,
            'book_name':bookss.book_name,
            'book_des':bookss.book_des,
            'author_id':bookss.author_id,
            'cat_id':bookss.cat_id
        })
        return{
            'message':'book details created',
            'book_id':bookss.book_id
        }
    
    async def retr_one(self,book_id):
        b=await self.collection.find_one({'book_id':book_id})
        if not b:
            return None
        b['_id']=str(b['_id'])
        auth=await self.author.find_one({'author_id':b['author_id']})
        if auth:
            auth["_id"]=str(auth['_id'])

        category=await self.cat.find_one({'cat_id':b['cat_id']})
        if category:
            category['_id']=str(category['_id'])
        
        return {
            'Book':b,
            'Author':auth,
            'Category':category
        }
    async def retireve_all(self,limit,page):
        t=await self.collection.count_documents({})
        skip=(page-1)*limit
        if  t>=skip or t==0:
            res= await self.collection.find().skip(skip).limit(limit).to_list(length=None)
            book=[]
            for r in res:
                r['_id']=str(r['_id'])
                book.append(r)
            return res
        else:
             raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Page number out of range"
    )   
    
    async def update(self,book_id,update):
        book = await self.collection.find_one({'book_id':book_id})
        if not book:
            return None
        res=await self.collection.update_one({'book_id':book_id},
                                        {"$set":update.dict()})
        return {
            'message':'updated',
            'book_id':str(book['_id'])
        }

    
    async def del_user(self,book_id):
        book=await self.collection.find_one({'book_id':book_id})
        if not book:
            return None
        await self.collection.delete_one({'book_id':book_id})
        return {
            'message':'Deleted'
        }