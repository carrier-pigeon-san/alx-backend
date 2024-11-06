#!/usr/bin/env python3
""" Basic Flask app, with a single route and an index.html template """
from flask import Flask, render_template, request
from flask_babel import Babel
import gettext as _

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


@babel.localeselector
def get_locale() -> str:
    """ Select a language translation to use for a request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_route() -> str:
    """ Returns a simple html page"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
