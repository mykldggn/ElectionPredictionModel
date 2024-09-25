# database.py
import sqlite3
import os

def get_connection(db_path='../data/election_data.db'):
    conn = sqlite3.connect(db_path)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    # Create tables if needed
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS polling_data (
            state TEXT,
            candidate_a REAL,
            candidate_b REAL,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
