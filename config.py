import os
app.config['SECRET_KEY'] = 'you-will-never-guess'
# ... add more variables here as needed

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'