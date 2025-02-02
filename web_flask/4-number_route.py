#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by
the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """The first function route, to return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """The second function route, to return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """The third function route, to display C with the <text> value"""
    return "C %s" % text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def p_text(text):
    """The fourth function route,
    to display Python with the <text> value provided"""
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Display <n is a number> if only n is a number"""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
