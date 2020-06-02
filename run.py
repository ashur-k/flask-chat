import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>To send a message use /USERNAME/MESSAGE</h1>'


@app.route('/<username>')
def username(username):
    return "<h3>Hello there " + username + " !</h3>"

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)

app.run(host=os.getenv('IP'), 
        port=int(os.getenv('PORT')),
        debug=True)