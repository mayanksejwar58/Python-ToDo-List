import streamlit as st
import time
from database.auth import Auth 

auth=Auth()

st.set_page_config(
  page_title="Sign-UP",
  page_icon="📝"
)
st.title("Create Account")
st.caption("Create Your Account to continue")

username=st.text_input("Username")
email=st.text_input("Email")
password=st.text_input("Password",type="password")

confirm=st.text_input("Confirm Password",type="password")

if st.button("Create Account"):
  if not username.strip():
    st.error("Username cannot be empty!")
  elif not email.strip():
    st.error("Email cannot be empty!")
  elif not password:
    st.error("Password cannot be empty")
  elif password!=confirm:
    st.error("Passwords do not match")
  else:
    result= auth.register(username,email,password)
    if result=="Success":
      st.success("Account Created")
      time.sleep(2)
      st.switch_page("pages/login.py")
    elif result=="Email Exists":
      st.error("Email ALready Registered")
    elif result=="Invalid Email":
      st.error("Invalid Email Format")
    elif result == "Weak Password":
      st.error(
        "Password must contain:\n"
        "- Minimum 8 Characters\n"
        "- Uppercase\n"
        "- Lowercase\n"
        "- Number"
        )

st.divider()
st.page_link(
  "pages/login.py",
  label="🔐 Already have an account? Login"
)