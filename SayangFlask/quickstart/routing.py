from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Ngarepan e'
@app.route('/hi')
def hi():
    return 'Iki kenalan'
