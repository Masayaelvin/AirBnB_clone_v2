#!/usr/bin/python3
"""
script that starts a Flask web application:
Routes:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Print a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb/', strict_slashes=False)
def display_HBNB():
    """
    Print a string
    """
    return 'HBNB'

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
