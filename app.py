import streamlit as st
from database.database import Database

db=Database()
db.create_table()

if"user"not in st.session_state:
  st.title("TO DO APP")
  page=st.sidebar.selectbox(
    "Menu",
    [
      "Login",
      "Register"
    ]
  )
  if page=="Login":
    st.switch_page("pages/login.py")
  else:
    st.switch_page("pages/register.py")
    
else:
  st.switch_page("pages/dashboard.py")
