from flask import Flask

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()
