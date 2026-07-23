import streamlit as st
from database.auth import Auth

st.set_page_config(
  page_icon="🔐",
  page_title="Login"
)
auth=Auth()

st.title("Login")
st.caption("Welcome Back")
email=st.text_input("Email")
password=st.text_input("Password",type="password")

if st.button("Login"):
  if not email.strip():
    st.error("Enter Email")
  elif not password:
    st.error("Enter Password")
  else:
    user=auth.login(
      email,
      password
    )
    if user:
      st.session_state.user=user
      st.switch_page("pages/dashboard.py")
      st.rerun()

    else:
      st.error("Invalid Email or Password")

st.page_link(
  "pages/forgot_password.py",
  label="Forgot Password?"
)