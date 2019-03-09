from google.appengine.ext import ndb

class Entry(ndb.Model):
    text = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

def add_new_entry(data):
    newEntry = Entry(text=data)
    newEntry.put()

def get_all_entries():
    entries = Entry.query().order(-Entry.timestamp).fetch()
    return entries

def already_exists(text):
    return Entry.query(Entry.text == text).fetch(1)

def get_matching_entries(search_text):
    entries = Entry.query(Entry.text==search_text).order().fetch()
    return entries