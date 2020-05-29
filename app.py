#initialize flask project 
from flask import Flask
app = flask(__name__)

@app.route('/')
def index():
    return 'hello there, this is my first website building with flask'


