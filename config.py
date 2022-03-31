from app import file_path


DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "senha-segura"
