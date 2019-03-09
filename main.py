from flask import Flask, render_template, request, current_app
from db_helper import add_new_entry, get_all_entries, already_exists, get_matching_entries

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all-text')
def all_text():
    entries = get_all_entries()

    return render_template(
        'all_entries.html',
        texts=entries)

@app.route('/', methods=['POST'])
def submission():
    text = request.form['text']
    if not already_exists(text):
        add_new_entry(text)
        feedback = "SUCCESS"
    else:
        feedback = "ERROR: Duplicate text entered!!!"

    return render_template('home.html',
        submit_feedback=feedback)

@app.route('/search', methods=['POST'])
def search():
    text = request.form['text']
    entries = get_matching_entries(text)

    return render_template(
        'search_result.html',
        results=entries)
