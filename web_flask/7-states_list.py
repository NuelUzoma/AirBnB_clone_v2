#!/usr/bin/python3
"""
Write a script that starts a Flask application. The script must be
listening on port 5000 on the route '/states_list', import storage
from models and storage.all function()
"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML Page only when it is called
    from storage.all('State')"""
    states = storage.all(State)
    s_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', s_states=s_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request
    with the storage.close()"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
