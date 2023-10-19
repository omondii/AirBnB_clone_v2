#!/usr/bin/python3
"""
Imported modules:
flask
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hnbn():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def text(text):
    text = text.replace("_"," ")
    return f"C {text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
