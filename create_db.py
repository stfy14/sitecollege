from flask import Flask
from models import User, Contacts, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {
    'contacts': 'sqlite:///contacts.db'
}
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print('Создана база данных users')
    with app.app_context():
        db.create_all('contacts')
    print('Создана база данных contacts')