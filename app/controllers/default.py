from app import app
from flask import render_template
from app.models.users import MyForm
from flask_mysqldb import MySQL
from app import mysql
import MySQLdb.cursors


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


@app.route('/usuarios')
def users():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM login;')
    result = cur.fetchall()
    return str(result)

