from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sergey:98432412@localhost:5432/books"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class BookModel(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, index=True, primary_key=True)
    isbn = db.Column(db.String(255))
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    pages = db.Column(db.Integer())
    year = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

if __name__ == '__main__':
    manager.run()