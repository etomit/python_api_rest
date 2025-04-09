
import sqlite3
import hashlib

def create_user_table():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def create_task_table():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS TASK (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        priority INTEGER,
        FOREIGN KEY (user_id) REFERENCES USER(id))''')
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    return hashlib.sha512(password.encode('utf-8')).hexdigest()
