#!/usr/bin/env python3
""" Basic Flask app, with a single route and an index.html template """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route() -> str:
    """ Returns a simple html page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
