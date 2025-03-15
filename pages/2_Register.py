import streamlit as st
from models import User, SessionLocal

st.title("Register for RecoverEase")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    with SessionLocal() as session:
        user_exists = session.query(User).filter_by(email=email).first()
        if user_exists:
            st.error("Email already exists.")
        else:
            new_user = User(username=username, email=email, password=password)
            session.add(new_user)
            session.commit()
            st.success(f"Account created successfully for {username}!")
