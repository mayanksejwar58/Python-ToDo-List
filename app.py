import streamlit as st
from database.database import Database

st.set_page_config(
  page_title="To-Do-App",
  page_icon="📝",
  layout="centered",
  initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"]{
display:none;
}
</style>
""", unsafe_allow_html=True)


if "user" in st.session_state:
  st.switch_page("pages/dashboard.py")

st.title("📝 ToDo List")
st.write("Stay Organized. Manage your tasks efficiently.")

col1,col2=st.columns(2)
with col1:
  if st.button("🔐 Login", use_container_width=True):
    st.switch_page("pages/login.py")

with col2:
  if st.button("📝 Sign Up", use_container_width=True):
    st.switch_page("pages/register.py")