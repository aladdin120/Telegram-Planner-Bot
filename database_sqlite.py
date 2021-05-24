import sqlite3

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS reminder(name TEXT, hours INTEGER, minute INTEGER, date INTEGER, 
    month INTEGER) """
    cursor.execute(query)
