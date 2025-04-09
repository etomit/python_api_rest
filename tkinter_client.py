import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
from app.services import task_service

API_URL = "http://localhost:8080"

def create_user():
    login = simpledialog.askstring("Login", "Entrez le login:")
    password = simpledialog.askstring("Password", "Entrez le mot de passe:", show="*")
    name = simpledialog.askstring("Name", "Entrez le nom:")

    if not (login and password and name):
        messagebox.showerror("Erreur", "Tous les champs sont requis.")
        return

    response = requests.post(f"{API_URL}/user", json={
        "login": login,
        "password": password,
        "name": name
    })

    if response.status_code == 200:
        user_id = response.json().get("id")
        messagebox.showinfo("Succès", f"Utilisateur créé avec l'ID: {user_id}")
    else:
        messagebox.showerror("Erreur", f"Erreur: {response.text}")

def list_users():
    response = requests.get(f"{API_URL}/user")
    if response.status_code == 200:
        users = response.json()
        msg = "\n".join([f"{u['id']} - {u['login']} - {u['name']}" for u in users])
        messagebox.showinfo("Utilisateurs", msg if msg else "Aucun utilisateur")
    else:
        messagebox.showerror("Erreur", f"Erreur: {response.text}")

def create_task():
    description = simpledialog.askstring("Description", "Description de la tâche:")
    status = simpledialog.askstring("Statut", "Statut:")
    priority = simpledialog.askinteger("Priorité", "Priorité (nombre):")
    user_id = simpledialog.askinteger("User ID", "ID de l'utilisateur assigné:")

    if not (description and status and priority is not None and user_id):
        messagebox.showerror("Erreur", "Tous les champs sont requis.")
        return

    task_service.add_task(user_id, description, status, priority)
    messagebox.showinfo("Succès", "Tâche créée avec succès.")

def list_tasks():
    user_id = simpledialog.askinteger("User ID", "ID de l'utilisateur (laisser vide pour tous):")
    tasks = task_service.get_tasks_by_user(user_id)
    msg = "\n".join([
        f"{t['id']} - {t['description']} (Priorité: {t['priority']}, Statut: {t['status']}, Utilisateur: {t['user_id']})"
        for t in tasks
    ])
    messagebox.showinfo("Tâches", msg if msg else "Aucune tâche")

# Interface principale
root = tk.Tk()
root.title("Client API Demo")

tk.Button(root, text="Créer un utilisateur", command=create_user, width=30).pack(pady=5)
tk.Button(root, text="Lister les utilisateurs", command=list_users, width=30).pack(pady=5)
tk.Button(root, text="Créer une tâche", command=create_task, width=30).pack(pady=5)
tk.Button(root, text="Lister les tâches", command=list_tasks, width=30).pack(pady=5)

root.mainloop()
