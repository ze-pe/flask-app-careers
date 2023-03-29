from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id': 1,
  'title': 'Data Analyst',
  'location': 'New York, NY',
  'salary': '$105,000'
  },
  {
  'id': 2,
  'title': 'Business Analyst',
  'location': 'Trenton, NJ',
  'salary': '$85,000'
  },
  {
  'id': 3,
  'title': 'UX Designer',
  'location': 'Remote',
  },
  {
  'id': 4,
  'title': 'Program Coordinator',
  'location': 'Columbus, OH',
  'salary': '$55,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    