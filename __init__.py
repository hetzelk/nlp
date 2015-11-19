from flask import Flask, render_template, redirect, request, url_for
import os
from DAO import DAO
from Wikipedia_API import Wikipedia_API

app = Flask(__name__)
dao = DAO()
api = Wikipedia_API()

@app.route('/index', methods= ['GET'])
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/training-set', methods = ['GET', 'POST'])
def training_set():
    try:
        titles = dao.find('topics', 'title')
        titles = [title.title() for title in titles]
        return render_template('training-set.html', titles = titles)
    except Exception as e:
        print(e)
    
@app.route('/write', methods=['POST'])
def write():
    user_input = request.form.get("user-input")
    return redirect(url_for('index'))

@app.route('/quote')
def quote():
    return render_template('quote.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT, 5000'))
    app.run(host = "10.2.20.12")