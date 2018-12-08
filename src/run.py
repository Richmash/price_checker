from src.app import app

__author___ = 'richmash'

app.run(debug=app.config['DEBUG'], port=4490)