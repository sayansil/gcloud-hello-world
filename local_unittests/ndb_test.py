import unittest
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from models.Entry import Entry

class DatastoreTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def testInsertEntity(self):
        text = 'Hello world', 'New world'
        Entry(text=text[0], tags=text[0].split()).put()
        Entry(text=text[1], tags=text[1].split()).put()
        self.assertEqual(2, len(Entry.get_all_entries()))

    def testExactSearch(self):
        text = 'Hello world', 'New world'
        Entry(text=text[0], tags=text[0].split()).put()
        Entry(text=text[1], tags=text[1].split()).put()
        search_text = 'Hello world'
        results = Entry.exact_search(search_text)
        self.assertEqual(1, len(results))
        self.assertEqual(search_text, results[0].text)

    def testKeywordSearch(self):
        text = 'Hello world', 'New world', 'Hello in ndb'
        Entry(text=text[0], tags=text[0].split()).put()
        Entry(text=text[1], tags=text[1].split()).put()
        Entry(text=text[2], tags=text[2].split()).put()
        search_text = 'world'
        results = Entry.keyword_search(search_text)
        self.assertEqual(2, len(results))
        search_text = 'ndb'
        results = Entry.keyword_search(search_text)
        self.assertEqual(1, len(results))
        self.assertEqual('Hello in ndb', results[0].text)

    def testDeleteEntity(self):
        text = 'Hello world'
        Entry(text=text, tags=text.split()).put()
        results = Entry.exact_search(text)
        self.assertEqual(1, len(results))
        results[0].delete_entry()
        results = Entry.exact_search(text)
        self.assertEqual(0, len(results))

if __name__ == '__main__':
    unittest.main()