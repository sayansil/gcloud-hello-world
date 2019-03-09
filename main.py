from flask import Flask, render_template, request, current_app
from datetime import datetime
from google.appengine.ext import ndb

app = Flask(__name__)

class Entry(ndb.Model):
    name = ndb.StringProperty()
    timestamp = ndb.StringProperty()

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
    name = request.form['name']
    data = {
            'name': name,
            'timestamp': unicode(datetime.utcnow())
        }
    push(data)
    return render_template('home.html')

def push(data):
    newEntry = Entry()
    newEntry.name = data['name']
    newEntry.timestamp = data['timestamp']
    newEntry.put()

def pull():
    entries = Entry.query().order(-Entry.timestamp).fetch()
    print entries
    return entries