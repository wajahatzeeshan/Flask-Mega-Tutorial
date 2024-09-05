from flask import Flask
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Wajahat Zeeshan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Karachi!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movies are so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)