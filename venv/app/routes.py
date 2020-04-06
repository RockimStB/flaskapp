from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rockim'}
    posts= [
        {
            'author': {'username':'John'},
            'body':'Beatiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body':'Beatiful day in Portland!'
        }
    ]
    return  render_template('index.html',title='Home', user=user, posts=posts)