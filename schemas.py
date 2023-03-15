from pydantic import BaseModel
from typing import List
from pydantic import EmailStr





class UserSchema(BaseModel):
    name:str
    email:EmailStr
    password:str

    class Config():
        orm_mode =True

class LoginSchema(BaseModel):
    email:EmailStr
    password:str

class ShowUser(UserSchema):
    blogs:List




class BlogSchema(BaseModel):
    title:str
    body:str
    user_id:int


    class Config:
        orm_mode =True

    


class ShowBlog(BlogSchema):
    title:str
    body:str
    creator:UserSchema



    