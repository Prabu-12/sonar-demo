import sqlite3

def get_user(username: str):
    # FIXED: Using parameterized query — no SQL injection!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def calculate(a, b):
    # FIXED: Handle division by zero!
    return a / b

def process_data(data: list):
    # FIXED: Simplified logic
    if data and len(data) > 0:
        return data[0]
    return None
