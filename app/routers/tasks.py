from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.create_task(db=db, task=task, user_id=current_user.id)

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    db_task = crud.get_task(db, task_id)
    if db_task is None or db_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.user_id == current_user.id).offset(skip).limit(limit).all()
    return tasks

@router.delete("/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    db_task = crud.get_task(db, task_id)
    if db_task is None or db_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task_id)
    return db_task

@router.put("/{task_id}", response_model=schemas.TaskBase)
def update_task(task_id: int, task: dict, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    db_task = crud.get_task(db, task_id)
    if db_task is None or db_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    print("Db task found")
    return crud.update_task(db, task_id, task)
