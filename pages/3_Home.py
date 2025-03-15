import streamlit as st
from models import LostItem, SessionLocal

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access this page.")
else:
    with SessionLocal() as session:
        lost_items = session.query(LostItem).all()

        if lost_items:
            table_data = [
                {
                    "Owner Name": item.owner_name,
                    "Description": item.item_desc,
                    "Last Seen Location": item.last_seen_location,
                    "Status": item.status,
                }
                for item in lost_items
            ]

            import pandas as pd

            df_table_data = pd.DataFrame(table_data)
            st.subheader("Lost Items")
            st.dataframe(df_table_data)
