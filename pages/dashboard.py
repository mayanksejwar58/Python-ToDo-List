import streamlit as st
from database.task_db import TaskDB

st.set_page_config(
  page_title="Dashboard",
  page_icon="📋",
  layout="wide"
)

if "user" not in st.session_state:
  st.warning("Please Login First")
  st.switch_page("pages/login.py")

db=TaskDB()
user=st.session_state.user

st.title(f"📋 Welcome {user['username']}")

total,completed,pending=db.statistics(user["id"])

progress=0
if total>0:
  progress=completed/total

st.progress(progress)
st.caption(f"{completed}/{total} Tasks Completed")

c1,c2,c3=st.columns(3)

c1.metric("📋 Total Tasks",total)
c2.metric("✅ Completed",completed)
c3.metric("⌛ Pending",pending)

st.divider()

st.subheader("➕ Add Task")

task=st.text_input("Task")

priority=st.selectbox(
  "Priority",
  ["High","Medium","Low"]
)

category=st.selectbox(
  "Category",
  ["Study","Work","Personal","Shopping","Health"]
)

due_date=st.date_input("Due Date")
due_time=st.time_input("Due Time")

if st.button("➕ Add Task"):

  if task.strip():
    db.add_task(
      user["id"],
      task,
      priority,
      category,
      str(due_date),
      str(due_time)
    )
    st.success("Task Added Successfully")
    st.rerun()
  else:
    st.error("Task cannot be empty!")

st.divider()

keyword=st.text_input("🔍 Search Task",placeholder="Search by task name...")

if keyword:
  tasks=db.search_task(user["id"],keyword)

else:
  tasks=db.get_tasks(user["id"])

if not tasks:
  st.info("No Tasks Found")
  st.stop()

st.subheader("Your Tasks")

for (task_id,task_name,completed,priority,category,due_date,due_time) in tasks:
  with st.container(border=True):
    st.markdown(f"### 📌 {task_name}")

    st.write(f"**Priority :** {priority}")
    st.write(f"**Category :** {category}")
    st.write(f"**📅 Due Date :** {due_date}")
    st.write(f"**🕒 Due Time :** {due_time}")

    status=st.checkbox(
      "Completed",
      value=bool(completed),
      key=f"status{task_id}"
    )
    if status!=bool(completed):
      db.toggle_task(
        task_id,
        int(status)
      )
      st.rerun()

    col1,col2=st.columns(2)
    if col1.button(
      "✏️ Edit",
      key=f"edit{task_id}"
    ):
      st.session_state.edit=(task_id,task_name)

    if col2.button("🗑 Delete",key=f"delete{task_id}"):
      st.session_state.delete=task_id

if "delete" in st.session_state:
  st.warning("Are you sure you want to delete this task?")
  c1,c2=st.columns(2)
  if c1.button("Yes"):
    db.delete_task(st.session_state.delete)
    del st.session_state.delete
    st.success("Task Deleted Successfully")
    st.rerun()

  if c2.button("No"):
    del st.session_state.delete
    st.rerun()

if "edit" in st.session_state:
  task_id,old_name=st.session_state.edit
  st.divider()
  st.subheader("✏️ Edit Task")

  new_name=st.text_input("Task Name",value=old_name)

  c1,c2=st.columns(2)
  if c1.button("Save"):
    if new_name.strip():
      db.edit_task(task_id,new_name)
      del st.session_state.edit
      st.success("Task Updated Successfully")
      st.rerun()
    else:
      st.error("Task cannot be empty!")

  if c2.button("Cancel"):
    del st.session_state.edit
    st.rerun()

st.divider()
with st.sidebar:
  st.header("👤 Account")
  st.write(f"**Username:** {user['username']}")
  st.write(f"**Email:** {user['email']}")
  st.divider()

  if st.button("🔒 Change Password"):
    st.switch_page("pages/change_password.py")

  if st.button("🚪 Logout"):
    del st.session_state.user
    st.switch_page("pages/login.py")