from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru',
  'salary': 1000000
}, {
  "id": 2,
  "title": "Data Scientist",
  "location": "New York, NY",
  "salary": 110000
}, {
  "id": 3,
  "title": "Marketing Manager",
  "location": "Los Angeles, CA",
}]


@app.route('/')
def index():
  return render_template('home.html', jobs=Jobs, company_name='Binay Blasters')


@app.route('/api/jobs')
def listjobs():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
