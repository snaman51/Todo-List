from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    deadline = Column(DateTime, default=None)
    priority = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="tasks")