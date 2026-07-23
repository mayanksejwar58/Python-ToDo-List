import sqlite3

class Database:

  def __init__(self):
    self.connection=sqlite3.connect(
      "todo.db",
      check_same_thread=False
    )

    self.connection.execute("PRAGMA foreign_keys=ON")
    self.cursor=self.connection.cursor()

  def create_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
      
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL
    )
    """)

    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      task TEXT NOT NULL,
      completed INTEGER DEFAULT 0,
      priority TEXT DEFAULT 'Medium',
      category TEXT DEFAULT 'General',
      due_date TEXT,
      due_time TEXT,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

      FOREIGN KEY(user_id)
      REFERENCES users(id)
      ON DELETE CASCADE

    )
    """)   
    self.connection.commit()

  def close(self):
    self.cursor.close()
    self.connection.close()