from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return'<html><body><h1><u><i>Hello Dude</i></u></h1></body></html>'
