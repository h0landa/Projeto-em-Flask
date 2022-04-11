from app import app
from flask import render_template, request
from app.models.users import LoginForm, RegisterForm
from app.models.tables import User, db


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def hello():
    Loginform = LoginForm()
    msg = ''
    login = ''
    if Loginform.validate_on_submit():
        login = User.query.filter_by(username=Loginform.username.data).first()
        if login and login.password == Loginform.data.password:
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
        login = User.query.filter_by(username=Registerform.username.data).first()
        if login:
            mensagem = 'Esse usuário já existe, tente novamente'
        else:
            new_user = User(f'{Registerform.username.data}', f'{Registerform.password.data}', f'{Registerform.email.data}', f'{Registerform.date.data}')        
            db.session.add(new_user)
            db.session.commit()
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
