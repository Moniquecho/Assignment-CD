# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/farm')
def farm():
    return 'Nice weather!'
    

