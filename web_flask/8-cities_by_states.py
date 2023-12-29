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


@app.route('/cities_by_states/', strict_slashes=False)
def cities_list():
    """
    Template html Cities
    """
    the_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', my_states=the_states)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
