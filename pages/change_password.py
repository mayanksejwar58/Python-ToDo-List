import streamlit as st
import bcrypt

from database.database import Database
st.set_page_config(page_title="Change Password")
if "user" not in st.session_state:
  st.switch_page("pages/login.py")

db=Database()
user=st.session_state.user
st.title("Change Password")

current=st.text_input(
  "Current Password",type="password"
)
new=st.text_input(
  "New Password",type="password"
)

confirm=st.text_input(
  "Confirm Password",type="password"
)

if st.button("Update Password"):
  if new!=confirm:
    st.error("Passwords do not match")
  else:
      db.cursor.execute(
        """
        SELECT password
        FROM users
        Where id=?
        """,
        (user["id"],)
      )
      stored =db.cursor.fetchone()

      if stored is None:
        st.error("User Not Found")
      elif bcrypt.checkpw(
        current.encode(),
        stored[0]
      ):
        new_hash=bcrypt.hashpw(
          new.encode(),
          bcrypt.gensalt()
        )
        db.cursor.execute(
          """
          UPDATE users
          SET password=?
          where id=?
          """,
          (new_hash,user["id"])
        )
        db.connection.commit()
        st.success("Password Changed Successfully")

      else:
       st.error("Current Password is Incorect")