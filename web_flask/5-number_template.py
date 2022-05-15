#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def returnhellohbn():
    '''to display'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def returnHBNB():
    ''' display hbnb'''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def f(text):
    """
    /c/<text>:  followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text_replace = text.replace("_", " ")
    return "C {}".format(text_replace)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Python followed by text
    """
    text_replace = text.replace("_", " ")
    return "Python {}".format(text_replace)


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """n is a  only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def displayhtml(n):
    '''display a HTML page only if n is an integer'''
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
