from flask import Flask,jsonify
from flask_cors import CORS

#configuration
DEBUG = True

#initialize flask project 
app = Flask(__name__)
app.config.from_object(__name__)

#enable cors
CORS(app,resources={r'/*': {'origin': '*'}})

@app.route('/ping',method=['GET'])
def index():
    return jsonify('pong')

if __name__ == '__main__':
    app.run()

