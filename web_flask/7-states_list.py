#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """List of cities states in storage"""
    return render_template("7-states_list.html", states=storage.all("State"))


@app.teardown_appcontext
def teardown(exc):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
