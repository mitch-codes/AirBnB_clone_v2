#!/usr/bin/python3
"""
use flask to generate and display
HTML pages
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ return hbn on index request """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
