#!/usr/bin/python3

from flask inport Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.route('/states/<id>', strict_slashes=False)
def display_states(state_id=None):
    all_states = stotage.all(State).values()
    all_cities = storage.all(City).values()
    if state_id == None:
        return render_template('templates/9-states.html', states=all_states)
    else:
        mystatelist = []
        tempcities = []
        for mystate in all_states:
            if mystate.id == state_id:
                mystatelist.append(mystate)
        myrealstate = mystatelist[0]
        for mycity in all_cities:
            if myrealstatelist.id == mycity.state_id:
                tempcities.append(mycity)

        return render_template('templates/9-states.html', statereal=myrealstate, cities=tempcities)

@app.teardown_appcontext
def db_close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
