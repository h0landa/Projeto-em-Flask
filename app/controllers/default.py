from app import app
from flask import Flask, render_template

@app.route('/')
def hello():
    return 'Index page'


@app.route('/form/')
def formulario():
    return render_template('form_page.html')


@app.route('/hello')
def hello_word():
    return f'Hello word!'


