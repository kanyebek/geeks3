import sqlite3
from config import DB_PATH 
from db import queries

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(queries.CREATE_TABLE_TASKS)
    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(queries.SELECT_TASKS)
    tasks = c.fetchall()
    conn.close()
    return tasks

def add_task(task):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(queries.INSERT_TASK, (task,))
    conn.commit()
    task_id = c.lastrowid
    conn.close()    
    return task_id


def update_task(task_id, new_task):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()    


def delete_task(task_id):   
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()
