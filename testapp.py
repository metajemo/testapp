import sqlite3
from flask import Flask, g, render_template
from contextlib import closing


DEBUG = True
DATABASE = 'testapp.db'
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect_db(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor.executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    ''' '''
    g.db = connect_db()

@app.teardown_request
def teardown_request():
    ''' '''
    db = getattr(g, 'db', None):
    if db is not None:
        db.close()

@app.route('/')
def index():
    #TODO - get the current db state and create/populate the template
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
