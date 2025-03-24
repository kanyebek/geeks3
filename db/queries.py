# queries.py

CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
"""

SELECT_TASKS = "SELECT id, task, created_at FROM task"

INSERT_TASK = "INSERT INTO task (task, created_at) VALUES (?, ?)"

UPDATE_TASK = "UPDATE task SET task = ?, created_at = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM task WHERE id = ?"
