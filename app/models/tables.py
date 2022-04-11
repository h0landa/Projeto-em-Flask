from enum import unique
from typing_extensions import Self
from app import db

class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    date = db.Column(db.DateTime)

    def __init__(self, username, password, email, date, id):
        self.username = username
        self.password = password
        self.id = id
        self.email = email
        self.date = date
    def __repr__(self):
        return "<User %r" % self.username
        