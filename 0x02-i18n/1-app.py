#!/usr/bin/env python3
""" Basic Flask app, with a single route and an index.html template """
from flask import Flask, render_template
from flask_babel import Babel

# Flask app instantiation
app = Flask(__name__)


# Config class for the app
class Config:
    """ Config class for the app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# app configuration using the Config class
app.config.from_object(Config)

# Babel object instantiation
babel = Babel(app)


@app.route('/', strict_slashes=False)
def hello_route() -> str:
    """ Returns a simple html page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)