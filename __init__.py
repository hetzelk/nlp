from flask import Flask, render_template, redirect, request, url_for
import os
from DAO import DAO
from Wikipedia_API import Wikipedia_API

app = Flask(__name__)
## dao = DAO()
## api = Wikipedia_API()

@app.route('/index', methods= ['GET'])
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/training-set', methods = ['GET', 'POST'])
def training_set():
    try:
        ## titles = dao.find('topics', 'title')
        ## titles = [title.title() for title in titles]
        return render_template('training-set.html')
    except Exception as e:
        print(e)
    
@app.route('/search', methods=['POST'])
def search():
    search = request.form.get("search")
    compare = Compare()
    context = {'searched': True, 'query_name': compare.query_name, 'results': compare.top}
    return redirect(url_for('index', **context))

@app.route('/quote')
def quote():
    return render_template('quote.html')

if __name__ == '__main__':
    app.run()