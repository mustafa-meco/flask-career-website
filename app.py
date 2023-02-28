from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Aswan, Egypt',
  'salary': 'EGP 10,000'
}, {
  'id': 2,
  'title': 'Data Scientest',
  'location': 'Cairo, Egypt',
  'salary': 'EGP 15,000'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Developer',
  'location': 'New York, USA',
  'salary': '$150,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Codha")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
