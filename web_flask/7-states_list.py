#!/usr/bin/python3

from flask import Flask
from flask import render_template
from models.db_storage import DBStorage
from models import storage

app = Flask(__name__)

@app.route('/state_list', strict_slashes=False)
def state_list():
    state_name = []
    state_id = []
    all_states = storage.all(State)
    for obj in all_states:
        state_name.append(obj.name)
        state_id.append(obj.id)
        return render_template('7-states_list.html', names=state_name, ids=state_id)

@app.teardown_appcontext
def db_close(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000')
