#!/usr/bin/env python3
""" Basic Flask app, with a single route and an index.html template """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import gettext as _
import pytz

# Flask app instantiation
app = Flask(__name__)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": "None", "timezone": "Europe/London"},
}


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
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('Accept-Language')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# get_timezone function that returns a timezone or None
@babel.timezoneselector
def get_timezone() -> str:
    """ Returns the timezone or None """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                return timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


# get_user function that returns a user dictionary or None
def get_user() -> dict:
    """ Returns a user dictionary or None if the ID cannot be found """
    login_as = request.args.get('login_as')
    if login_as and int(login_as) in users:
        return users.get(int(login_as))
    return None


# before_request handler that finds a user and sets it as a global on `g.user`
@app.before_request
def before_request():
    """ Finds a user and sets it as a global on `g.user` """
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route('/', strict_slashes=False)
def hello_route() -> str:
    """ Returns a simple html page"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
