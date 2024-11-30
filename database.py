import sqlite3

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()
sql_query = """ CREATE TABLE IF NOT EXISTS jobs (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           title VARCHAR(250) NOT NULL,
           location VARCHAR(250) NOT NULL,
           salary INTEGER,
           currency VARCHAR(10),
           responsibility TEXT,
           requirements TEXT
           )
        """
cursor.execute(sql_query)

ds_desc = """The responsibilities of a Data Scientist include gathering, cleaning, and preparing large, complex datasets from various sources to ensure quality and consistency for analysis.
Applying statistical techniques, machine learning algorithms, and predictive models to analyze data and generate insights.
Working with big data technologies (e.g., Hadoop, Spark) and cloud platforms (e.g., AWS, Google Cloud) to handle and analyze large-scale datasets.
Developing automated solutions to improve data workflows, reduce manual work, and increase efficiency."""

ds_req = '''A Bachelor's or Master's degree in Computer Science, Data Science, Mathematics, Statistics, Engineering, or a related field.
Python, R, or similar languages for data analysis and model development.
Strong skills in data manipulation libraries (e.g., Pandas, NumPy) and statistical analysis.
Familiarity with tools like Hadoop, Spark, or similar platforms for handling large datasets.'''

da_desc = '''Responsiblity as a Data Analyst are collecting, cleaning, and analyzing data to provide insights that help businesses make informed decisions.
Key tasks include data gathering from various sources, performing statistical analysis, creating reports and visualizations, and collaborating 
with different teams to address business needs. '''

da_req = '''To be eligible for the Data Analyst position, candidates should have a bachelor''s degree in a relevant field such as Data Science, Mathematics, or Economics.
 Proficiency in data analysis tools like SQL, Excel, Python, or R is essential, along with experience in data visualization tools such as Tableau or Power BI.
 Strong analytical, problem-solving, and communication skills are necessary to interpret data and present insights to stakeholders'''
 
be_desc = '''Design, develop, and maintain the backend of web applications, ensuring high performance, scalability, and reliability.
Write clean, reusable, and efficient code that follows industry best practices and coding standards.
Work closely with frontend engineers to integrate the backend systems with the user interface.
Ensure smooth and seamless interaction between client-side and server-side applications.'''

be_req = '''Bachelor's or Master's Degree in Computer Science, Software Engineering, Information Technology, or a related field.
Strong proficiency in backend programming languages such as Java, Python, Ruby, PHP or Go.
Familiarity with object-oriented programming (OOP) principles and design patterns.
Knowledge of backend frameworks such as Spring Boot (Java), Django (Python), Flask (Python), Ruby on Rails.
Experience with API development frameworks and tools, including RESTful APIs.''' 

cursor.execute(""" INSERT INTO jobs (title, location, salary, currency, responsibility, requirements) VALUES (?, ?, ?, ?, ?, ?)""", 
               ('Data Scientist', 'Bhubaneswar, India', 150000, 'INR', ds_desc, ds_req))
			   
cursor.execute(""" INSERT INTO jobs (title, location, salary, currency, responsibility, requirements) VALUES (?, ?, ?, ?, ?, ?)""", 
              ('Data Analyst', 'Hyderabad, India', 100000, 'INR', da_desc, da_req))			

cursor.execute(""" INSERT INTO jobs (title, location, salary, currency, responsibility, requirements) VALUES (?, ?, ?, ?, ?, ?) """,
              ('Backend Engineer', 'Pune, India', 120000, 'INR', be_desc, be_req))			  

# Commit changes to save them to the database
conn.commit()

# Close the connection
conn.close()
