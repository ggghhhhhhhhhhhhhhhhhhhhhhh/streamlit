import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import LostItem

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

    st.title("Report Lost Item")

    # Input fields for reporting a lost item
    owner_name = st.text_input("Owner Name")
    item_desc = st.text_area("Item Description")
    last_seen_location = st.text_input("Last Seen Location")
    image_url = st.text_input("Image URL (optional)")

    if st.button("Submit Report"):
        with SessionLocal() as session:
            # Add new lost item to the database
            new_item = LostItem(
                owner_name=owner_name,
                item_desc=item_desc,
                last_seen_location=last_seen_location,
                image_url=image_url,
                status="Lost"
            )
            session.add(new_item)
            session.commit()
            st.success(f"Lost item reported successfully for {owner_name}!")
