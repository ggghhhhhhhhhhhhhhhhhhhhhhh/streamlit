import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import FoundItem

# Initialize database connection
engine = create_engine('sqlite:///instance/recoverease.db')
SessionLocal = sessionmaker(bind=engine)

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
    st.markdown("[Go to Login Page](./1_Login)")
else:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False  # Reset login state
        st.experimental_set_query_params(page="login")  # Redirect to login page

    st.title("Report Found Item")

    # Input fields for reporting a found item
    finder_name = st.text_input("Finder Name")
    contact_info = st.text_input("Contact Info")
    item_desc = st.text_area("Item Description")
    found_location = st.text_input("Found Location")

    if st.button("Submit Report"):
        with SessionLocal() as session:
            # Add new found item to the database
            new_item = FoundItem(
                finder_name=finder_name,
                contact_info=contact_info,
                item_desc=item_desc,
                found_location=found_location,
            )
            session.add(new_item)
            session.commit()
            st.success(f"Found item reported successfully by {finder_name}!")
