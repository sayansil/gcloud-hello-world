from flask import Flask, render_template, request, current_app
from datetime import datetime
from google.cloud import datastore

app = Flask(__name__)

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
    ds = datastore.Client('s4d-test')
    key = ds.key('Text')

    entity = datastore.Entity(key=key)
    entity.update(data)
    ds.put(entity)

def pull():
    ds = datastore.Client('s4d-test')
    query = ds.query(kind='Text', order=['-timestamp'])

    query_iterator = query.fetch()
    entities = list(query_iterator)

    return entities