#!/usr/bin/python3
"""
Task 1 flask web
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """returns hello hbnh!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
