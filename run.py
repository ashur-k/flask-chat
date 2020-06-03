import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []

    #Add messages to the messages list
def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}){}: {}".format(now, username, message))

def get_all_messages():
    #Get all of the messages and separate them with a br
    return '<br>'.join(messages)


@app.route('/')
def index():
    #main page with instructions
    return render_template('index.html')


@app.route('/<username>')
def user(username):
    #display chat messages
    print(datetime.now().time())
    return "<h1>Welcome, {0}:-</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    #create a new messsage and redirect back to the chat page
    add_messages(username, message)
    return redirect('/' + username)  

app.run(host=os.getenv('IP'), 
        port=int(os.getenv('PORT')),
        debug=True)