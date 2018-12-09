from flask import Flask, render_template, request, session, make_response
from src.common.database import Database

__author___ = 'richmash'


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def hello_world():
    return "Hello world!"



from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
