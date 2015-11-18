from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

@app.route('/index', methods=['GET'])
@app.route('/', methods =['GET'])
def index():
	return render_template('index.html')

@app.route('/write', methods=['POST'])
def write():
	user_input = request.form("user-input")
	return redirect 

if __name__ == '__main__':
	port = int(os.environ.get('PORT, 5000'))
    app.run(host = "10.2.20.12", port = port, debug = True)