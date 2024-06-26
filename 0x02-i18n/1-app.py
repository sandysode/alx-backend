#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask
from flask import render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render a html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
