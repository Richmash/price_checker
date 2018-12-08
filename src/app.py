from flask import Flask

__author___ = 'richmash'


app = Flask(__name__)
app.congig.from_object('config')

@app.route('/')
def hello_world():
    return "Hello world!"

