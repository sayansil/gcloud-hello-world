from google.appengine.ext import ndb

class Entry(ndb.Model):
    text = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    tags = ndb.StringProperty(repeated=True)

    def delete_entry(self):
        self.key.delete()

    def put_entry(self):
        self.put()

def add_new_entry(data):
    if not already_exists(data):
        Entry(text=data, tags=data.split()).put_entry()
        return "SUCCESS"
    return "ERROR: Duplicate text entered!!!"

def get_all_entries():
    entries = Entry.query().order(-Entry.timestamp).fetch()
    return entries

def already_exists(text):
    return Entry.query(Entry.text == text).fetch(1)

def exact_search(search_text):
    entries = Entry.query(Entry.text==search_text).fetch()
    return entries

def keyword_search(search_text):
    entries = Entry.query(Entry.tags.IN(search_text.split())).fetch()
    return entries

def delete_all():
    ndb.delete_multi(Entry.query().fetch(keys_only=True))


