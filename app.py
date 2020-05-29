#initialize flask project 
import flask from Flask
app = flask(__name__)

@app.route('/')
def index():
    return 'hello there, this is my first website building with flask'


