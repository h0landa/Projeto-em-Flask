from app import app
from flask import render_template

from app.models.users import MyForm

@app.route('/')
def hello():
    return 'Index page'


@app.route('/form/')
def formulario():
    form = MyForm()
    return render_template('form_page.html',
                            form=form)


@app.route('/hello')
def hello_word():
    return f'Hello word!'


