import streamlit as st
from models import User, SessionLocal

st.title("Login to RecoverEase")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    with SessionLocal() as session:
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid username or password.")

