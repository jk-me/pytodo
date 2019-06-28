from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Jenny'}
    todos = [
        {
            'author': {'username': 'John'},
            'body': 'Go for a run!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Bake a cake'
        }
    ]
    return render_template('index.html', title='Home', user=user, todos=todos)
