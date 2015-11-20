from flask import Flask, render_template, redirect, request, url_for
import os
from DAO import DAO
from Wikipedia_API import Wikipedia_API
import sys, traceback
from run_comparison import Compare

app = Flask(__name__)
## dao = DAO()

@app.route('/index', methods = ['GET'])
@app.route('/', methods = ['GET'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        traceback(e)
        
@app.route('/training-set', methods = ['GET', 'POST'])
def training_set():
    try:
        ## titles = dao.find('topics', 'title')
        ## titles = [title.title() for title in titles]
        return render_template('training-set.html')
    except Exception as e:
        traceback(e)
    
@app.route('/search', methods = ['POST'])
def search():
    try:
        search = request.form.get("search")
        comparison = Compare()
        context = {'searched': True, 'query_name': compare.query_name, 'results': compare.top}
        return redirect(url_for('index'))
    except Exception as e:
        traceback(e)

@app.route('/quote')
def quote():
    try:
        return render_template('quote.html')
    except Exception as e:
        traceback(e)
    
def traceback(e):
    ex_type, ex, tb = sys.exc_info()
    traceback.print_tb(tb)
    print("Error: {} | Type: {}".format(e, type(e)))

if __name__ == '__main__':
    app.run()