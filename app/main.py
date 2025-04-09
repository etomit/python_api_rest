
from fastapi import FastAPI, HTTPException
from app.services.user_service import create_user_table, create_task_table
from app.repositories.user_repository import get_all_users, get_user_by_id, create_user, update_user, delete_user
from app.models.user import UserCreate, UserUpdate
from app.init_db import initialize_database
import sqlite3
initialize_database()
app = FastAPI()

@app.on_event("startup")
def startup():
    create_user_table()
    create_task_table()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Demo"}

@app.get("/user")
def read_users():
    return get_all_users()

@app.post("/user")
def create(user: UserCreate):
    return {"id": create_user(user)}

@app.get("/user/{user_id}")
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

@app.put("/user/{user_id}")
def update(user_id: int, user: UserUpdate):
    if update_user(user_id, user):
        return {"message": "Utilisateur mis à jour"}
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

@app.delete("/user/{user_id}")
def delete(user_id: int):
    if delete_user(user_id):
        return {"message": "Utilisateur supprimé"}
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

from app.models.task import Task
from app.repositories import task_repository

@app.post("/task")
def create_task(task: Task):
    task_id = task_repository.create_task(
        task.description, task.status, task.priority, task.user_id
    )
    return {"id": task_id}

@app.get("/task")
def read_tasks():
    return task_repository.get_tasks()

@app.get("/task/{task_id}")
def read_task(task_id: int):
    task = task_repository.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return dict(task)

@app.put("/task/{task_id}")
def update_task(task_id: int, task: Task):
    task_repository.update_task(task_id, task.description, task.status, task.priority)
    return {"message": "Task updated successfully"}

@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    task_repository.delete_task(task_id)
    return {"message": "Task deleted successfully"}

