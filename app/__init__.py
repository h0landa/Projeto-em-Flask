from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os


file_path = os.path.abspath(os.getcwd())+"\dados.db"
app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object('config')
manager = Manager(app)
manager.add_command('db', MigrateCommand)
mysql = MySQL(app)


from app.controllers import default 
