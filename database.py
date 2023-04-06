from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# establish connectivity (need to install pymysql)
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
    "ssl_cert": "/etc/ssl/cert.pem"
    }
  }
)

# set up connection, give connection a name, use that connection to execute commands in the db, the with keyword automatically closed the connection after the commands are executed
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    jobs = []
    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val").params(val=id))
    column_names = result.keys()
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(zip(column_names, rows[0]))

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 {"job_id": job_id,
                 "full_name": data['full_name'],
                 "email": data['email'],
                 "linkedin_url":data['linkedin_url'],
                 "education":data['education'],
                 "work_experience": data['work_experience'],
                 "resume_url": data['resume_url']}
                 ) 