#!/usr/bin/python3
"""
A script that starts a Flask Web application
with a port connecting to port 5000
"""


from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display the states and cities list"""
    all_states = storage.all(State)
    s_states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=s_states)


@app.teardown_appcontext
def teardown(exception):
    """This function that closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
