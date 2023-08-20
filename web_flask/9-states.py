#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """show list of states in storage"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """show list of states ids in storage"""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
