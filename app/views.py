from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    content = {'title': 'Hello,',
               'body': ['Hello world!']}
    
    return render_template('index.html',
                           content=content)