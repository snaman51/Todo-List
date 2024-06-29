from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str = ""
    description: str = ""
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None