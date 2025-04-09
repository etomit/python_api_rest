import sqlite3

def get_db_connection():
    conn = sqlite3.connect("demo.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_task(description, status, priority, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO task (description, status, priority, user_id) VALUES (?, ?, ?, ?)",
        (description, status, priority, user_id),
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM task").fetchall()
    conn.close()
    return tasks

def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute("SELECT * FROM task WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return task

def update_task(task_id, description, status, priority):
    conn = get_db_connection()
    conn.execute(
        "UPDATE task SET description = ?, status = ?, priority = ? WHERE id = ?",
        (description, status, priority, task_id),
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM task WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
