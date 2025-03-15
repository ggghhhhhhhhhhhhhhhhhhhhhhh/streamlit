import os
from sqlalchemy import create_engine
from models import Base

# Ensure 'instance' directory exists
os.makedirs('instance', exist_ok=True)

# Create SQLite database file
DATABASE_URL = "sqlite:///instance/recoverease.db"
engine = create_engine(DATABASE_URL)

# Create all tables defined in models.py
Base.metadata.create_all(engine)

print("Database and tables created successfully.")
