from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    username = StringField('Nome', validators=[DataRequired()])
    date = DateField('Data de Nascimento', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])

    