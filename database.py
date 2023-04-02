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