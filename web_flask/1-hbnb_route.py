#!/usr/bin/python3
# 1-hbnb_route.py

'''Script that starts a web application'''

# import flask class from flask module
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
