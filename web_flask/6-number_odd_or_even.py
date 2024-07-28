#!/usr/bin/python3
# 6-number_odd_or_even.py


'''Script that starts a web application'''

# import flask class from flask module
# import render_template for rendering templates to browser
from flask import Flask, render_template

# create an instance called app of the class by passing __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''display "Hello HBNB!"

    Returns:
        str: text on the index page
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''displays "HBNB"

    Returns:
        str : text on the hbnb page
    '''
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """display "C", followed by the value of the text variable

    Args:
        text (str): text to be served on the page

    Returns:
        str: text on the page
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    '''display “Python ”, followed by the value of the text variable

    Args:
        text (str, optional) : text on page. Default is cool

    Returns:
        str: text on page
    '''

    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    '''display "{n} is a number"

    Args:
        n (int): number to be served on the page

    Returns:
        str: text on the page
    '''
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    '''displays a HTML page only if n is an integer

    Args:
        n (int): number to be displayed

    Returns:
        str: text on html page
    '''
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''display a HTML page only if n is an integer

    Args:
        n (integer): number to be displayed on page

    Returns:
        str: text on the page
    '''
    eod = 'even' if n % 2 == 0 else 'odd'

    return render_template('6-number_odd_or_even.html', num=n, odd_even=eod)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
