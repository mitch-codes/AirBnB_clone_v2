#!/usr/bin/python3

from flask import Flask
from flask import render_template

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
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def numberOdd(n):
    if isinstance(n, int):
        if n%2 == 0:
            values = {
                'value1': n,
                'value2': 'even'
            }
            return render_template('6-number_odd_or_even.html', **values)
        else:
            values = {
                'value1': n,
                'value2': 'odd'
            }
            return render_template('6-number_odd_or_even.html', **values)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
