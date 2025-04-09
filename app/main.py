
from fastapi import FastAPI, HTTPException
from app.services.user_service import create_user_table, create_task_table
from app.repositories.user_repository import get_all_users, get_user_by_id, create_user, update_user, delete_user
from app.models.user import UserCreate, UserUpdate
import sqlite3

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
