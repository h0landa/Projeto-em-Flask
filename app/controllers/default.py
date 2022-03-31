from crypt import methods
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
    if form.validate_on_submit():
        print(f'Nome de usuário: {form.username}')
        print(f'Email de usuário: {form.email}')
    return render_template('form_page.html', methods = 'POST, GET', 
                        form=form)
    
    

@app.route('/hello', defaults={'name':None})
@app.route('/hello/<name>')
def hello_word(name):
    if name:
        return f'Olá, %s!' % name
    else:
        return f'Olá,usuário!'

