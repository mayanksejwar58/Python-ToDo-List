from database.database import Database

class TaskDB:

  def __init__(self):
    self.db=Database()

  def add_task(self,user_id,task,priority,category,due_date,due_time):
    self.db.cursor.execute(
      """
      Insert INTO tasks(user_id,task,priority,category,due_date,due_time)
      Values(?,?,?,?,?,?)
      """,
      (user_id,task,priority,category,due_date,due_time)
    )
    self.db.connection.commit()

  def get_tasks(self,user_id):
    self.db.cursor.execute(
      """
      SELECT id,task,completed,priority,category,due_date,due_time
      FROM tasks
      WHERE user_id=?
      ORDER BY due_date,due_time
      """,
      (user_id,)
    )
    return self.db.cursor.fetchall()

  def delete_task(self,task_id):
    self.db.cursor.execute(
      """
      DELETE FROM tasks
      WHERE id=?
      """,
      (task_id,)
    )
    self.db.connection.commit()

  def toggle_task(self,task_id,completed):
    self.db.cursor.execute("""
      UPDATE TASKS
      SET completed=?
      WHERE id=?
      """,
      (completed,task_id)
    )
    self.db.connection.commit()

  def edit_task(self, task_id, task):
    self.db.cursor.execute("""
    UPDATE tasks
    SET task=?
    WHERE id=?
    """,
    (task, task_id)
    )
    self.db.connection.commit()

  def search_task(self,user_id,keyword):
    self.db.cursor.execute("""
    SELECT id,task,completed,priority,category,due_date,due_time
    FROM tasks
    WHERE user_id=?
    AND task LIKE?
    ORDER BY due_date,due_time
    """,
    (user_id,f"%{keyword}%")
    )
    return self.db.cursor.fetchall()
  def statistics(self, user_id):
    self.db.cursor.execute(
    "SELECT COUNT(*) FROM tasks WHERE user_id=?",
    (user_id,)
    )
    total = self.db.cursor.fetchone()[0]

    self.db.cursor.execute(
    """
    SELECT COUNT(*)
    FROM tasks
    WHERE user_id=?
    AND completed=1
    """,
    (user_id,)
    )
    completed = self.db.cursor.fetchone()[0]
    pending=total-completed
    return total,completed,pending
  