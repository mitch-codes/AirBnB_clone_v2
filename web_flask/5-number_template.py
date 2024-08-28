#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return "HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "c {}".format(text)

@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return "python {}".format(text)

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return n

@app.route('/number_template/<n>', strict_slashes=False):
def number_template():
    if isinstance(n, int):
        return "<!DOCTYPE html>
<HTML lang='en'>
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {}</H1>
    </BODY>
</HTML>".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
