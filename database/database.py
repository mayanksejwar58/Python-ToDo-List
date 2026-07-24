from supabase import create_client
import streamlit as st

class Database:
  
  def __init__(self):
    self.supabase = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )
  def get_client(self):
    return self.supabase