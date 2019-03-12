from flask import Flask, render_template, request, current_app
from models import Entry
import unit_tests

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# All entries
@app.route('/all-text')
def all_text():
    entries = Entry.get_all_entries()
    return render_template(
        'all_entries.html',
        texts=entries)

# Add a new entry after duplicate check
@app.route('/', methods=['POST'])
def submission():
    text = request.form['text']
    feedback = Entry.add_new_entry(text)
    return render_template('home.html',
        submit_feedback=feedback)

# Perform keyword based search
@app.route('/search', methods=['POST'])
def search():
    text = request.form['text']
    entries = Entry.keyword_search(text)
    return render_template(
        'search_result.html',
        results=entries)

# Delete all entries
@app.route('/cleared')
def cleared():
    Entry.delete_all()
    return render_template('home.html')


######################### UNIT TESTS ########################

@app.route('/unit-tests')
def unit_test():
    return render_template(
        'unit_tests.html')

@app.route('/unit-test1')
def unit_test1():
    return render_template(
            'unit_tests.html',
            result_1=unit_tests.unit_test1())

@app.route('/unit-test2')
def unit_test2():
    return render_template(
            'unit_tests.html',
            result_2=unit_tests.unit_test2())

@app.route('/unit-test3')
def unit_test3():
    return render_template(
            'unit_tests.html',
            result_3=unit_tests.unit_test3())

@app.route('/unit-test4')
def unit_test4():
    return render_template(
            'unit_tests.html',
            result_4=unit_tests.unit_test4())

#############################################################