from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)



def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("jobs.db")
    except sqlite3.error as e:
        print(e)
    return conn   

def load_jobs_from_db():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    result = cursor.fetchall()
    job_list = []
    # Column names to use as keys for the dictionary
    columns = ["id", "title", "location", "salary", "currency", "responsibility", "requirements"]
    
    for row in result:
        job_dict = dict(zip(columns, row))  # Convert each row to a dictionary
        job_list.append(job_dict)
    
    return job_list

def load_job_db(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE id = ?", (id,))
    result = cursor.fetchall()

    if len(result) == 0:
        return None
    else:            
        # Column names to use as keys for the dictionary
        columns = ["id", "title", "location", "salary", "currency", "responsibility", "requirements"]

        for row in result:
            job_list = dict(zip(columns, row))  # Convert each row to a dictionary

        return job_list
    
def add_application_to_db(id, data):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO application (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                   (id, data['name'], data['email'], data['linkedin'], data['education'], data['experience'], data['resume']))

    conn.commit()
    conn.close()

def add_contact_to_db(data):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO contact (name, email, message) VALUES (?, ?, ?)""", (data['name'], data['email'], data['message']))

    conn.commit()
    conn.close()

    


@app.route("/")
def hello_world():
    job_list = load_jobs_from_db()
    return render_template('home.html', jobs=job_list)

@app.route("/about")
def about_us():
    return render_template('about_us.html')

@app.route("/contact")
def contact_us():
    return render_template('contact.html')


@app.route("/api/jobs")
def job_list_api():
    job_list = load_jobs_from_db()
    return jsonify(job_list)

@app.route("/api/jobs/<int:id>")
def job_id(id):
    job = load_job_db(id)
    if not job:  # If no job is found for the given ID
        return ("ERROR: Job not found"), 404
    return render_template('jobpage.html', job=job)
    #return jsonify(job)

@app.route("/api/jobs/<int:id>/apply", methods=['POST'])
def apply_job(id):
    data = request.form
    job_list = load_job_db(id)
    add_application_to_db(id, data)
    return render_template('app_submited.html', application=data, job=job_list)

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        data={
            "name":name,
            "email":email,
            "message":message
        }
        add_contact_to_db(data)

        return "Successfully submitted"

    return render_template('contact.html')    
  

if __name__ == '__main__':
    app.run(debug=True)