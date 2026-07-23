from storage import Storage
from models.task import Task

class TaskManager:
    def __init__(self):
        self.storage=Storage()
        self.tasks=self.storage.load_task()

    def add_task(self,name):
        task=Task(name)
        self.tasks.append(task)
        self.storage.save_task(self.tasks)
        print("Task Added Successfully")

    def view_tasks(self):
        if not self.tasks:
            print("\n No Task Found! \n")
            return
        print("\n------Task List------\n")

        for index,task in enumerate(self.tasks,start=1):
            status="Done" if task.completed else "Not Done"
            print(f"{index}.{task.name}[{status}]")

    def delete_task(self,index):
        if 0<index<=len(self.tasks):
            self.tasks.pop(index-1)
            self.storage.save_task(self.tasks)
            print("Task Deleted")

        else:
            print("Please enter valid number of task")

    def edit_task(self,index,new_name):
        if 0<index<=len(self.tasks):
            self.tasks[index-1].edit(new_name)
            self.storage.save_task(self.tasks)
            print("Task Updated")
        else:
            print ("Invalid Task Number")

    def toggle_task(self,index):

        if 0<index<=len(self.tasks):
            self.tasks[index-1].toggle()
            self.storage.save_task(self.tasks)
            print("Task Status Updated")
        else:
            print ("Invalid Task Number")
    def search_task(self,keyword):
        found=False
        print("\nSearch Results\n")

        for index, task in enumerate(self.tasks,start=1):
            if keyword.lower() in task.name.lower():
                status="Done" if task.completed else "Not Done"
                print(f"{index}. {task.name} [{status}]")
                found=True

        if not found:
            print("No Matching Task Found.")