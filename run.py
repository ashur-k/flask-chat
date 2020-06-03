import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

    #Add messages to the messages list
def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    #Get all of the messages and separate them with a br
    return '<br>'.join(messages)


@app.route('/')
def index():
    #main page with instructions
    return '<h1>To send a message use /USERNAME/MESSAGE</h1>'


@app.route('/<username>')
def user(username):
    #display chat messages
    return "<h1>Welcome, {0}:-</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    #create a new messsage and redirect back to the chat page
    add_messages(username, message)
    return redirect('/' + username)  

app.run(host=os.getenv('IP'), 
        port=int(os.getenv('PORT')),
        debug=True)