from app import app
from flask import render_template
from app.forms import LoginForm 


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
            'body':'Beatiful day in Grenada!'
        }
    ]
    return  render_template('index.html',title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form =LoginForm()
    return render_template('login.html', title='Sign In' ,form=form)