import sqlite3
from flask import Flask, g, render_template
from contextlib import closing
#TODO add option to populate entries

DEBUG = True
DATABASE = 'testapp.db'
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


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
def teardown_request(exception):
    ''' '''
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    c = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=title, text=text) for title, text in c.fetchall()]
    return render_template('index.html', entries=entries)
if __name__ == '__main__':
    app.run()
