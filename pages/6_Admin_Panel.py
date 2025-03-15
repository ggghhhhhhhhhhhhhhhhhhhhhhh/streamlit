import streamlit as st
from models import LostItem, FoundItem, SessionLocal

if not (st.session_state.get("logged_in", False) and 
        (st.session_state.current_user == "admin")):
    st.warning("Only admins can access this page.")
else:
    with SessionLocal() as session:
        lost_items=session.query(LostItems.all())
