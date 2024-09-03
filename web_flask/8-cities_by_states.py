#!/usr/bin/python3

from flask inport Flask
from flask import render_template
from models import storage

@app.route('/cities_by_states')
def cities_by_states():
    state_dict = {}
    all_states = stotage.all(State).values()
    all_cities = storage.all(City).values()
    for mystate in all_states:
        tempcities = []
        for mycity in all_cities:
            if mystate.id == mycity.state_id:
                tempcities.append(mycity)
        state_dict[mystate.id] = tempcities

    return render_template('', states=all_states, state_dict=state_dict)

@app.teardown_appcontext
def db_close(exception):
    storage.close()
