
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Blog(Base):
    __tablename__="blogs"
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey("user.id"))

    creator = relationship("User", back_populates="blogs")


    # def __repr__(self) -> str:
    #     return self.title



class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email= Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


    blogs = relationship("Blog", back_populates="creator")

