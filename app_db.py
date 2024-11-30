import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Execute the query to create the table
'''sql_query = """ CREATE TABLE IF NOT EXISTS application (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           job_id INTEGER NOT NULL,
           full_name VARCHAR(250) NOT NULL,
           email VARCHAR(250) NOT NULL,
           linkedin_url VARCHAR(500),
           work_experience TEXT,
           education TEXT,
           resume_url VARCHAR(500)
           );
        """'''
#cursor.execute(sql_query)

cursor.execute("SELECT * FROM application")
result = cursor.fetchall()

print(result)

# Commit the transaction and close the connection
conn.commit()
conn.close()
