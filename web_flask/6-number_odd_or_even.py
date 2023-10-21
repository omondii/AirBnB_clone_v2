#!/usr/bin/python3
"""
Imported modules
flask
render_template
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return "Not a valid number"


@app.route("/number_template/<int:n>", strict_slashes=True)
def template(n):
    if isinstance(n, int):
        return render_template('5-number.html')
    else:
        return "Not a valid number"

    
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddEven(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', number=n)
    else:
        return "Not a valid number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
