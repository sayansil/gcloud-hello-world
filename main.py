from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/submission', methods=['POST'])
def submission():
    name = request.form['name']
    return render_template(
        'submission.html',
        name=name)