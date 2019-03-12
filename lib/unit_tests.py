from models.Entry import add_new_entry, exact_search, keyword_search

def unit_test1():
    # test 1 : Add new entries
    text = 'Hello world'
    result1 = 'SUCCESS' == add_new_entry(text)
    text = 'New world'
    result2 = 'SUCCESS' == add_new_entry(text)
    return result1 and result2

def unit_test2():
    # # test 2 : Search exact match
    text = 'Hello world'
    result3 = len(exact_search(text)) is not 0
    text = 'New world'
    result4 = len(exact_search(text)) is not 0
    return result3 and result4

def unit_test3():
    # test 3 : Search keywords
    text = 'world'
    result5 = 'Hello world' in [entry.text for entry in keyword_search(text)]
    result6 = 'New world' in [entry.text for entry in keyword_search(text)]
    return result5 and result6

def unit_test4():
    # test 4 : Delete the new entries
    text = 'Hello world'
    entries = exact_search(text)
    if entries == []:
        result7 = False
    else:
        entries[0].delete_entry()
        result7 = len(exact_search(text)) is 0
    text = 'New world'
    entries = exact_search(text)
    if entries == []:
        result8 = False
    else:
        entries[0].delete_entry()
        result8 = len(exact_search(text)) is 0
    return result7 and result8