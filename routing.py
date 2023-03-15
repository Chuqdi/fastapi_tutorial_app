

from sqlalchemy.orm import Session
from database import get_db
from jwtHandler import JWTHandler
from schemas import BlogSchema, ShowBlog, ShowUser, UserSchema, LoginSchema
from Hasher import Hasher
from fastapi import APIRouter, Body, HTTPException
from fastapi import  Depends, status
import models
from jwtBearer import JwtBearer


userRouter = APIRouter(
    prefix="/user"
)
blogRouter = APIRouter()





@blogRouter.post("/blog", dependencies=[Depends(JwtBearer())], tags =["blogs"], response_model=ShowBlog)
def test(blog:BlogSchema, db:Session= Depends(get_db)):
    new_blog = models.Blog(title = blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog






@userRouter.post("/sign_up", tags=['users'], status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def user(user:UserSchema, db:Session=Depends(get_db)):
    new_user = models.User(name = user.name, email = user.email, password=Hasher.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@userRouter.post("/login", tags=["users"], status_code=status.HTTP_200_OK,)
async def login(user:LoginSchema=Body(default=None), db:Session=Depends(get_db)):
    user_d = db.query(models.User).filter(models.User.email == user.email).first()
    if not user_d:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Invalid Email Credentials")
    
    if not Hasher.deCrypt(user.password, user_d.password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Invalid Password Credentials")
    print(user_d)
    
    return {
        "token_access":JWTHandler.encode(user_d.id)
    }

