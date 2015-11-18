from flask import Flask, render_template, redirect, request, url_for
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print(type(e))
        print(e)
    
if __name__ == '__main__':
    ## port = int(os.environ.get('PORT, 5000'))
    ## app.run(host = "10.2.20.12")
    app.run()