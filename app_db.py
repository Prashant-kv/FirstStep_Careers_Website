import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Execute the query to create the table
sql_query = """ CREATE TABLE IF NOT EXISTS contact (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(250) NOT NULL,
           email VARCHAR(250) NOT NULL,
           message TEXT
           );
        """
cursor.execute(sql_query)

conn.commit()
conn.close()
