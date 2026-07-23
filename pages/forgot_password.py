import streamlit as st
import random
import bcrypt
import time

from database.database import Database
from database.email_service import send_otp

db = Database()

st.title("Forgot Password")

email = st.text_input("Enter Email")

if st.button("Send OTP"):
  db.cursor.execute(
    "SELECT id FROM users WHERE email=?",
    (email,)
  )
  user = db.cursor.fetchone()

  if user:
    otp = str(random.randint(100000,999999))
    status=send_otp(email,otp)
    if status:
      st.session_state.otp = otp
      st.session_state.otp_time=time.time()
      st.session_state.attempt=0
      st.session_state.reset_email=email

      st.success("OTP sent to your email")
    else:
      st.error("Unable to send OTP")
  else:
    st.error("Email Not Found")
  
otp = st.text_input("Enter OTP")

new_password = st.text_input(
    "New Password",
    type="password"
)

if st.button("Reset Password"):
  if "otp" not in st.session_state:
    st.error("Generate OTP First")
  elif time.time()-st.session_state.otp_time>300:
    st.error("OTP Expired")
  else:
    st.session_state.attempt+=1

    if st.session_state.attempt>5:
      st.error("Maximum Attempt Reached")
    elif otp!=st.session_state.otp:
      st.error("Invalid OTP")
    elif not new_password:
      st.error("Enter New Password")
    else:
      hashed = bcrypt.hashpw(
        new_password.encode(),
        bcrypt.gensalt()
      )
      db.cursor.execute("""
        UPDATE users
        SET password=?
        WHERE email=?
      """,
      (
        hashed,
        st.session_state.reset_email
      )
      )
      db.connection.commit()

      del st.session_state.otp
      del st.session_state.otp_time
      del st.session_state.attempt
      del st.session_state.reset_email
      st.success("Password Reset Successful")
      
      time.sleep(2)
      st.switch_page("pages/login.py")
      st.stop()
      db.close()
