#!/usr/bin/python3
# 0-hello_route.py

'''Script that starts a web application'''

# im port flask class from flask module
from flask import Flask

# create an instance called app of the class by passing __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
