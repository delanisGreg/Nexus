from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/')
def index():
    name = "This is the route."
    return name

@app.route('/hello')
def hello():
    name = "Hello world!"
    return name

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0')
