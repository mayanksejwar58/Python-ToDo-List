import streamlit as st
import bcrypt
from database.database import Database

st.set_page_config(
  page_title="Change Password",
  initial_sidebar_state="collapsed"
)
if "user" not in st.session_state:
  st.switch_page("pages/login.py")

client=Database().get_client()
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
      result = (
        client.table("users")
        .select("password")
        .eq("id", user["id"])
        .execute()
        )
      if not result.data:
        st.error("User Not Found")
        st.stop()

      stored = result.data[0]["password"]

      if stored is None:
        st.error("User Not Found")
      elif bcrypt.checkpw(
        current.encode(),
        stored.encode()
      ):
        new_hash=bcrypt.hashpw(
          new.encode(),
          bcrypt.gensalt()
        )
        client.table("users").update({
          "password":bcrypt.hashpw(
            new.encode(),
            bcrypt.gensalt()
          ).decode()

        }).eq(
          "id",
          user["id"]
        ).execute()
      
        st.success("Password Changed Successfully")

      else:
       st.error("Current Password is Incorect")