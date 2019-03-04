from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all-text')
def server_time():
    return render_template(
        'server_time.html',
        time=str(datetime.now()))

@app.route('/submission', methods=['POST'])
def submission():
    name = request.form['name']
    return render_template(
        'submission.html',
        name=name)


