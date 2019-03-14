from flask import Flask, render_template, request, current_app
from models.Entry import Entry

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# All entries
@app.route('/all-text')
def all_text():
    entries = Entry.get_all_entries()
    return render_template(
        'all_entries.html',
        texts=entries)

# Add a new entry after duplicate check
@app.route('/', methods=['POST'])
def submission():
    text = request.form['text']
    if not Entry.already_exists(text):
        Entry(text=text, tags=text.split()).put()
        feedback = 'SUCCESS'
    else:
        feedback = 'ERROR: Duplicate text entered!!!'
    return render_template('home.html',
        submit_feedback=feedback)

# Perform keyword based search
@app.route('/search', methods=['POST'])
def search():
    text = request.form['text']
    entries = Entry.keyword_search(text)
    return render_template(
        'search_result.html',
        results=entries)

# Delete all entries
@app.route('/cleared')
def cleared():
    Entry.delete_all()
    return render_template('home.html')
