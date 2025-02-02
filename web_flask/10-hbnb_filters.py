#!/usr/bin/python3
"""
A script that starts a Flask web app with the following
displays a like-wise HTML Page with 6-index.html
"""


from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Display a HTML page like 6-index.html"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
