from email.policy import default
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


@app.route('/hello', defaults={'name':None})
@app.route('/hello/<name>')
def hello_word(name):
    if name:
        return f'Olá, %s!' % name
    else:
        return f'Olá,usuário!'

