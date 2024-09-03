#!/usr/bin/python3

from flask inport Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
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

    return render_template('templates/8-cities_by_states.html', states=all_states, state_dict=state_dict)

@app.teardown_appcontext
def db_close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
