from models.Entry import Entry

def unit_test1():
    # test 1 : Add new entries
    text = 'Hello world'
    if Entry.already_exists(text):
        result1 = False
    else:
        Entry(text=text, tags=text.split()).put()
        result1 = True
    text = 'New world'
    if Entry.already_exists(text):
        result2 = False
    else:
        Entry(text=text, tags=text.split()).put()
        result2 = True
    return result1 and result2

def unit_test2():
    # # test 2 : Search exact match
    text = 'Hello world'
    result3 = len(Entry.exact_search(text)) is not 0
    text = 'New world'
    result4 = len(Entry.exact_search(text)) is not 0
    return result3 and result4

def unit_test3():
    # test 3 : Search keywords
    text = 'world'
    result5 = 'Hello world' in [entry.text for entry in Entry.keyword_search(text)]
    result6 = 'New world' in [entry.text for entry in Entry.keyword_search(text)]
    return result5 and result6

def unit_test4():
    # test 4 : Delete the new entries
    text = 'Hello world'
    entries = Entry.exact_search(text)
    if entries == []:
        result7 = False
    else:
        entries[0].delete_entry()
        result7 = len(Entry.exact_search(text)) is 0
    text = 'New world'
    entries = Entry.exact_search(text)
    if entries == []:
        result8 = False
    else:
        entries[0].delete_entry()
        result8 = len(Entry.exact_search(text)) is 0
    return result7 and result8