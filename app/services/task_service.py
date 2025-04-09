import sqlite3

def add_task(user_id: int, description: str, status: str, priority: int = None):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO TASK (user_id, description, status, priority)
                      VALUES (?, ?, ?, ?)''', (user_id, description, status, priority))
    conn.commit()
    conn.close()

def get_tasks_by_user(user_id: int):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT id, description, status, priority FROM TASK WHERE user_id = ?''', (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id: int, status: str):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE TASK SET status = ? WHERE id = ?''', (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id: int):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM TASK WHERE id = ?''', (task_id,))
    conn.commit()
    conn.close()
