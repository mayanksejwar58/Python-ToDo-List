tasks=[]

def show_tasks(tasks):
  print("\n"+"="*45)
  print(f"{'No.':<5}{'Status':<10}{'Task'}")
  print("="*45)

  for index,task in enumerate(tasks,start=1):
    status="✅" if task["completed"] else "❌"
    print(f"{index:<5}{status:<10}{task['name']}")
  
  print("="*45+"\n")

def no_task(tasks):
  if not tasks:
    print("There Is No Task")
    return True
  return False
def add_task(tasks, task):
  new_task={
    "name":task,
    "completed":False
  }
  tasks.append(new_task)
  print("Task Added Successfully!")

def delete_task(tasks):
  if no_task(tasks):
    return
  
  show_tasks(tasks)
  try:
    task_number=int(input("Enter Task Number To Delete: "))
  except ValueError:
    print("Please Enter Valid Task Number")
    return
  if 1<=task_number<=len(tasks):
    deleted_task=tasks.pop(task_number-1)
    print(f"'{deleted_task['name']}' Deleted Successfully!")
  else:
    print("Invalid Task Number")
  
def mark_task(tasks):
  if no_task(tasks):
    return
  show_tasks(tasks)
  try:    
    task_number=int(input("Enter Task Number: "))
  except ValueError:
    print("Please Enter Valid Task Number")
    return
  
  if 1<=task_number<=len(tasks):
    if tasks[task_number-1]["completed"]:
      tasks[task_number-1]["completed"]=False
      print("Marked task as Icomplete")
    else:
      tasks[task_number-1]["completed"]=True
      print("Marked task as Complete")
  else:
    print("Invalid Task Number")

def edit_task(tasks):
  if no_task(tasks):
    return
  show_tasks(tasks)
  try:
    number=int(input("Enter Task Number: "))
  except ValueError:
    print("Please Enter Valid Task Number")  
    return
  if 1<=number<=len(tasks):
    new_name=input("Enter New Name of the Task: ")
    tasks[number-1]["name"]=new_name
    print("Task Updated Successfully")
  else:
    print("Invalid Task Number")


while True:
  print("******TO-DO-List******")
  print("1. Add Task")
  print("2. View Task")
  print("3. Delete Task")
  print("4. Mark The Task")
  print("5. Edit Task")
  print("6. Exit")


  choice=input(" Enter Your Choice:-  ")

  if choice =="1":
    task=input("Enter Task: ").strip()
    if not task:
      print ("Task cannot be empty!")
      continue
    add_task(tasks,task)
    
  elif choice=="2":
    if no_task(tasks):
      continue
    show_tasks(tasks)

  elif choice=="3":
    delete_task(tasks)

  elif choice=="4":
    mark_task(tasks)
  
  elif choice=="5":
    edit_task(tasks)

  elif choice=="6":
    print("Thank You For Using TO-DO-List😊😊")
    break
  else :
    print("Invalid Choice")


