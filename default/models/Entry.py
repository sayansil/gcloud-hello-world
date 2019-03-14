from google.appengine.ext import ndb

class Entry(ndb.Model):
    text = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    tags = ndb.StringProperty(repeated=True)

    def delete_entry(self):
        self.key.delete()

    @classmethod
    def delete_all(cls):
        ndb.delete_multi(cls.query().fetch(keys_only=True))

    @classmethod
    def get_all_entries(cls):
        entries = cls.query().order(-cls.timestamp).fetch()
        return entries

    @classmethod
    def already_exists(cls, text):
        return cls.query(cls.text == text).fetch(1)

    @classmethod
    def exact_search(cls, search_text):
        entries = cls.query(cls.text==search_text).fetch()
        return entries

    @classmethod
    def keyword_search(cls, search_text):
        entries = cls.query(cls.tags.IN(search_text.split())).fetch()
        return entries



