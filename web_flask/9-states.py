#!/usr/bin/python3
"""
script that starts a Flask web application:
States and cities
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function to remove SQLAlchemy Session
    """
    storage.close()


@app.route('/states/', strict_slashes=False)
def states_list():
    """
    Template html Cities
    """
    the_states = storage.all(State).values()
    return render_template('7-states_list.html', my_states=the_states)


@app.route('/states/<number>', strict_slashes=False)
def cities_list(number):
    """
    Template html Cities
    """
    the_states = storage.all(State)
    state_id = 'State.{}'.format(number)
    if state_id in the_states:
        the_states = the_states[state_id]
    else:
        the_states = None
    return render_template('9-states.html', my_states=the_states)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
