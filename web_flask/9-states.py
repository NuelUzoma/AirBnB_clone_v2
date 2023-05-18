#!/usr/bin/python3
"""
This module provides a script for starting a Flask web application.
The web application listens on the IP address 0.0.0.0 and port 5000.
It utilizes a storage engine (either FileStorage or DBStorage)
to fetch data from a data source. The module ensures that the SQLAlchemy
session is properly handled and closed after each request.
"""


from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    all_states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html',
                           states=all_states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
