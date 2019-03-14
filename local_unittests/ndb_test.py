import unittest
from google.appengine.ext import ndb
from google.appengine.ext import testbed

class TestModel(ndb.Model):
    text = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    tags = ndb.StringProperty(repeated=True)

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
        TestModel(text=text[0], tags=text[0].split()).put()
        TestModel(text=text[1], tags=text[1].split()).put()
        self.assertEqual(2, len(TestModel.query().fetch(3)))

    def testExactSearch(self):
        text = 'Hello world', 'New world'
        TestModel(text=text[0], tags=text[0].split()).put()
        TestModel(text=text[1], tags=text[1].split()).put()
        search_text = 'Hello world'
        results = TestModel.query(TestModel.text==search_text).fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual(search_text, results[0].text)

    def testKeywordSearch(self):
        text = 'Hello world', 'New world', 'Hello in ndb'
        TestModel(text=text[0], tags=text[0].split()).put()
        TestModel(text=text[1], tags=text[1].split()).put()
        TestModel(text=text[2], tags=text[2].split()).put()
        search_text = 'world'
        results = TestModel.query(TestModel.tags.IN(search_text.split())).fetch(3)
        self.assertEqual(2, len(results))
        search_text = 'ndb'
        results = TestModel.query(TestModel.tags.IN(search_text.split())).fetch(3)
        self.assertEqual(1, len(results))
        self.assertEqual('Hello in ndb', results[0].text)

    def testDeleteEntity(self):
        text = 'Hello world'
        TestModel(text=text, tags=text.split()).put()
        results = TestModel.query(TestModel.text==text).fetch(2)
        self.assertEqual(1, len(results))
        results[0].key.delete()
        results = TestModel.query(TestModel.text==text).fetch(2)
        self.assertEqual(0, len(results))

if __name__ == '__main__':
    unittest.main()