import os
import sqlite3

def get_user(username):
    # VULNERABILITY: SQL Injection!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def calculate(a, b):
    # BUG: Division by zero possible!
    result = a / b
    return result

def unused_function():
    # CODE SMELL: Dead code
    pass

password = "admin123"  # VULNERABILITY: Hardcoded password!

def process_data(data):
    if data:
        if len(data) > 0:
            if data[0]:
                return data[0]
