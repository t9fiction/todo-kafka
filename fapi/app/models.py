from sqlmodel import Field, SQLModel
from typing import Optional
from app.engine_file import engine

######################################################################
# Class USERBASE
# class UserBase(SQLModel):
#     username: str = Field(index=True, unique=True)
#     name: str
#     is_active: bool = True
    
# class Users(UserBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     # hashed_password: str = Field()
#     password: str = Field(nullable=False)
#     # orders: list["Order"] = Relationship(back_populates="username")
#     # orders : int  | None = Field(default=None, foreign_key="order.id")

#     # def __str__(self):
#     #     return f"<User {self.username}>"
    
# class UserPassword(UserBase):
#     password: str = Field(nullable=False)

######################################################################
    
class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    content: str = Field(index=True)
    
######################################################################
######################################################################
    
class TodoPost(SQLModel, table=False):
    name: str = Field(index=True)
    content: str = Field(index=True)
    
######################################################################
