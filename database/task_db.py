from database.database import Database

class TaskDB:

  def __init__(self):
    self.db=Database().get_client()

  def add_task(self,user_id,task,priority,category,due_date,due_time):
    self.db.table("tasks").insert({
      "user_id": user_id,
      "task": task,
      "priority": priority,
      "category": category,
      "due_date": str(due_date),
      "due_time": str(due_time),
      "completed": False
    }).execute()

  def get_tasks(self,user_id):
    result=(
      self.db
      .table("tasks")
      .select("*")
      .eq("user_id",user_id)
      .order("due_date")
      .order("due_time")
      .execute()
    )
    tasks=[]
    for row in result.data:
      tasks.append(
        (
          row["id"],
          row["task"],
          row["completed"],
          row["priority"],
          row["category"],
          row["due_date"],
          row["due_time"]
        )
      )
    return tasks

  def delete_task(self,task_id):
    self.db.table("tasks")\
    .delete()\
    .eq("id",task_id)\
    .execute()

  def toggle_task(self,task_id,completed):
    self.db.table("tasks")\
    .update({
      "completed":completed
    })\
    .eq("id",task_id)\
    .execute()

  def edit_task(self, task_id, task):
    self.db.table("tasks")\
    .update({
      "task":task
    })\
    .eq("id",task_id)\
    .execute()

  def search_task(self,user_id,keyword):
    result=(
      self.db
      .table("tasks")
      .select("*")
      .eq("user_id", user_id)
      .ilike("task", f"%{keyword}%")
      .order("due_date")
      .order("due_time")
      .execute()
    )
    tasks=[]
    for row in result.data:
      tasks.append(
        (
          row["id"],
          row["task"],
          row["completed"],
          row["priority"],
          row["category"],
          row["due_date"],
          row["due_time"]
        )
      )
    return tasks
    
  def statistics(self, user_id):
    result=(
      self.db
      .table("tasks")
      .select("completed")
      .eq("user_id",user_id)
      .execute()
    )
    total=len(result.data)
    completed=sum(
      1 for row in result.data
      if row["completed"]
    )
    pending=total-completed
    return(total,completed,pending)