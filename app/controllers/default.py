import email
from app import app
from flask import render_template, request
from app.models.users import MyForm
from flask_mysqldb import MySQL
from app import mysql
import MySQLdb.cursors


@app.route('/')
def hello():
    return 'Index page'


@app.route('/form/', methods = ['POST', 'GET'])
def formulario():
    form = MyForm()
    if form.validate_on_submit():
        print(f'Nome de usuário: {form.username}')
        print(f'Email de usuário: {form.email}')
    if request.method == 'POST':
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        user = form.username
        password = form.password
        email = form.email
        date = form.date
        #cur.execute(f'INSERT INTO login(username, password, email, date) VALUES(\'{user}\', \'{password}\', \'{email}\', \'{date}\')')
        print('Data:', date)
    return render_template('form_page.html', 
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

