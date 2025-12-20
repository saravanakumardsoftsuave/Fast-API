from fastapi import HTTPException,status
from service.security import hash_password,verify_password
class user_class:
    def __init__(self, db):
        self.collection = db['user_create']

    async def user_create(self, user):
        exist = await self.collection.find_one({'email': user.email})
        if exist:
            return None
        hashed_password=hash_password(user.password)
        res=await self.collection.insert_one({
            'user_id':user.user_id,
            'name': user.name,
            'email': user.email,
            'password':hashed_password,
            'review_count':user.review_count,
            
        })
        
        return {"message": "mail created",
                "user_id": str(res.inserted_id)}
    
    async def login(self,gmail,password):
        user=await self.collection.find_one({'email':gmail})
        if not user:
            return{'message':'invalid email'}
        pass_word=verify_password(password,user['password'])
        if not pass_word:
            return {'message':'wrong pass'}
        return user
    
    async def user_retireve(self,limit,page):
        total=await self.collection.count_documents({})
        skip=(page-1)*limit
        if skip<=total:
            users=self.collection.find().skip(skip).limit(limit)
            if not users:
                return None
            res=[]
            async for user in users:
                user['_id']=str(user['_id'])
                res.append(user)
            return res
        else:
             raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Page number out of range"
    )   
    
    async def user_ret(self,email):
        user=await self.collection.find_one({
            'email':email,
        })
        users=[]
        if not user:
            return None
        user['_id'] = str(user['_id'])
        return {
            'message':'finded',
            'user_id':str(user.get('_id'))
        }
    

    async def update_user(self, email, update):
        user = await self.collection.find_one({'email': email})
        if not user:
            return None
        new = update.dict()
        await self.collection.update_one({"email": email},{"$set": new})
        return {
        "message": "Updated successfully",
        "User_id": str(new["_id"])}

    

    async def del_user(self,email):
        user=await self.collection.find_one({'email':email})
        if not user:
            return None
        new=self.collection.delete_one({'email':email})
        return {
            'message':'Deleted'
        }
        