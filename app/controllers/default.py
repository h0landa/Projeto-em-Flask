import email
from app import app
from flask import render_template, request
from app.models.users import LoginForm, RegisterForm



@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def hello():
    Loginform = LoginForm()
    msg = ''
    login = ''
    if Loginform.validate_on_submit():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        email = Loginform.email.data
        password = Loginform.password.data
        cur.execute(f"SELECT * FROM login WHERE email='{email}' and password = '{password}';")
        login = cur.fetchall()
        if login:
            return render_template('main_page.html')
        else:
            msg = 'Usuário/Senha Incorretos. Tente novamente'
    return render_template('login_page.html', Loginform = Loginform, msg = msg)


@app.route('/form/', methods=['POST', 'GET'])
def formulario():
    Registerform = RegisterForm()
    mensagem = ''
    login = ''    
    if request.method == 'POST':
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        user = Registerform.username.data
        password = Registerform.password.data
        email = Registerform.email.data
        date = Registerform.date.data
        cur.execute(f"SELECT * FROM login WHERE username = '{user}';")
        login = cur.fetchall()
        if login:
            mensagem = 'Esse usuário já existe, tente novamente'
        else:
            cur.execute(
                f"INSERT INTO login(username, password, email, date) VALUES('{user}', '{password}', '{email}', '{date}');")
            mysql.connection.commit()
            mensagem = 'Usuário cadastrado com sucesso'
    return render_template('form_page.html',
                           Registerform = Registerform, mensagem = mensagem)


@app.route('/hello', defaults={'name': None})
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
