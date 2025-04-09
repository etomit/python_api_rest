
import tkinter as tk
import requests

def add_user():
    login = entry_login.get()
    password = entry_password.get()
    name = entry_name.get()
    response = requests.post("http://localhost:8000/user", json={
        "login": login,
        "password": password,
        "name": name
    })
    label_result.config(text=response.text)

root = tk.Tk()
root.title("Client API")

tk.Label(root, text="Login").pack()
entry_login = tk.Entry(root)
entry_login.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Button(root, text="Ajouter utilisateur", command=add_user).pack()
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
