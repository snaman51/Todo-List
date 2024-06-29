from fastapi import FastAPI
from .database import engine
from . import models
from .routers import tasks, auth, users
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

