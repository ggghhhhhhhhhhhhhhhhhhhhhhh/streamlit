# app.py
import streamlit as st
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
import streamlit_authenticator as stauth

DATABASE_URL = "sqlite:///recoverease.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

from models import User, LostItem, FoundItem

Base.metadata.create_all(engine)

# Authentication setup
import streamlit_authenticator as stauth

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {u.username: {"email": u.email, "name": u.username, "password": u.password} for u in db.query(User).all()}

users_db = get_users()
credentials = {
    "usernames": {
        user.username: {
            "email": user.email,
            "name": user.username,
            "password": user.password
        } for user in get_users()
    }
}

authenticator = stauth.Authenticate(credentials=credentials,
                                    cookie_name="recoverease_cookie",
                                    key="some_signature_key",
                                    cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.write(f"Welcome *{name}*")

elif authentication_status == False:
    st.error("Username/password incorrect")
elif authentication_status is None:
    st.warning("Please enter your credentials")

if authentication_status:
    
    ## Step 3: Main Streamlit App (app.py)
    
    import streamlit as st
    
    st.title("RecoverEase - Lost & Found Items")
    
    menu_options = ["Home", "Report Lost Item", "Report Found Item", "Admin Panel"]
    
    if st.sidebar.button("Logout"):
        authenticator.logout('Logout', 'sidebar')
        st.experimental_rerun()
    
    choice = st.sidebar.selectbox("Menu", menu_options)
    
    if choice == "Home":
        db = SessionLocal()
        lost_items = db.query(LostItem).all()
        if lost_items:
            for item in lost_items:
                st.subheader(item.owner_name)
                st.write(f"Description: {item.item_desc}")
                st.write(f"Last Seen Location: {item.last_seen_location}")
                st.write(f"Status: {item.status}")
                if item.image_url:
                    st.image(item.image_url)
                st.divider()
        else:
            st.write("No lost items reported yet.")
    
        db.close()
    
    elif menu_options == "Report Lost Item":
        with st.form(key='report_lost_form'):
            owner_name = st.text_input("Owner Name")
            item_desc = st.text_area("Item Description")
            last_seen_location = st.text_input("Last Seen Location")
            image_url = st.text_input("Image URL (optional)")
            
            submit_lost_item = st.form_submit_button("Submit Report")
            
            if submit_lost_item:
                db.add(LostItem(owner_name=owner_name,
                                item_desc=item_desc,
                                last_seen_location=last_seen_location,
                                image_url=image_url,
                                user_id=current_user.id))
                db.commit()
                st.success("Lost item reported successfully!")
    
        # Report Found Item Form
        with st.form(key='found_item_form'):
            finder_name = st.text_input("Finder Name")
            contact_info = st.text_input("Contact Info")
            found_item_desc = st.text_area("Found Item Description")
            found_location = st.text_input("Found Location")
            
            submit_found_item = st.form_submit_button("Submit Found Report")
            
            if submit_found_item:
                new_found_item = FoundItem(
                    finder_name=finder_name,
                    contact_info=contact_info,
                    item_desc=found_item_desc,
                    found_location=found_location,
                    user_id=current_user.id
                )
                db.add(new_found_item)
                db.commit()
                st.success("Found item reported successfully!")

## Step 4: Admin Management Page
Streamlit can provide admin access based on the user's session state:

