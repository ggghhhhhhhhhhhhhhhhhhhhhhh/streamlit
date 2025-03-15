import os
import sqlite3

# Ensure the 'instance' directory exists
os.makedirs('instance', exist_ok=True)

# Connect to the SQLite database
connection = sqlite3.connect('instance/recoverease.db')
cursor = connection.cursor()

# Create tables if they do not exist
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lost_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_name TEXT NOT NULL,
            item_desc TEXT NOT NULL,
            last_seen_location TEXT NOT NULL,
            image_url TEXT,
            status TEXT DEFAULT 'Lost'
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS found_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            finder_name TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            item_desc TEXT NOT NULL,
            found_location TEXT NOT NULL
        );
    ''')

    connection.commit()
    print("Database initialized successfully.")
except Exception as e:
    print(f"An error occurred while initializing the database: {e}")
finally:
    connection.close()
