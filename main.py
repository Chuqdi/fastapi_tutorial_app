import models
from database import engine
from fastapi import FastAPI
from routing import userRouter, blogRouter



models.Base.metadata.create_all(engine)




app =FastAPI()

app.include_router(userRouter)
app.include_router(blogRouter)







