from enum import unique
from sqlalchemy import true
from app import db

class User(db.Model):
    __tablename__ = "login"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45))
    email = db.Column(db.String(120), unique=True)
    date = db.Column(db.DateTime)

    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return True


    @property
    def is_anonymous(self):
        return False
    

    def get_id(self):
        str(self.id)


    def __init__(self, username, password, email, date):
        self.username = username
        self.password = password
        self.email = email
        self.date = date
    def __repr__(self):
        return "<User %r" % self.username
        