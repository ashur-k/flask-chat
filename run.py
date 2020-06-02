import os
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return '<h1>Hello Wrold, just checking out</h1>'


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))