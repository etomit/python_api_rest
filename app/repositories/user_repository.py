
import sqlite3

def get_connection():
    return sqlite3.connect("demo.db")

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER")
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE id=?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO USER (login, password, name) VALUES (?, ?, ?)", 
                   (user.login, user.password, user.name))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def update_user(user_id, user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE USER SET login=?, password=?, name=? WHERE id=?", 
                   (user.login, user.password, user.name, user_id))
    updated = cursor.rowcount
    conn.commit()
    conn.close()
    return updated > 0

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USER WHERE id=?", (user_id,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
