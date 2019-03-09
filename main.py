from flask import Flask, render_template, request, current_app
from google.appengine.ext import ndb

app = Flask(__name__)

class Entry(ndb.Model):
    text = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all-text')
def all_text():
    texts = pull()
    return render_template(
        'all_entries.html',
        texts=texts)

@app.route('/', methods=['POST'])
def submission():
    text = request.form['text']
    push(text)
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    text = request.form['text']
    entries = pull()
    entries = [entry for entry in entries if entry.text == text]
    return render_template(
        'search_result.html',
        results=entries)

def push(data):
    newEntry = Entry(text=data)
    newEntry.put()

def pull():
    entries = Entry.query().order(-Entry.timestamp).fetch()
    return entries