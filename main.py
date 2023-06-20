# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

@app.route('/')
def index():
    return 'hi!There!'

@app.route('/farm')
def farm():
    return 'Cow and cat!'
    

