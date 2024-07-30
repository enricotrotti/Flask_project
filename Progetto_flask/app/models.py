from . import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# Qui usiamo SQLite, che crea un file db.sqlite e usa quello.
# db_url = 'sqlite:///db.sqlite'
# Oppure per usare MySQL; di solito host sarà 'localhost'
# e port sarà 3306. Creare il DB in anticipo, vuoto, senza tabelle.
# Nel caso: pip install mysql-connector-python
db_url = 'mysql+mysqlconnector://root:trottienrico010@localhost:3306/conference'

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Talk(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Speaker = db.Column(db.String(100))
    Start = db.Column(db.String(100), nullable=False)
    Duration = db.Column(db.Integer, nullable=False)
    Title = db.Column(db.String(100), nullable=False)
    Area = db.Column(db.String(100), nullable=False)
    Pdf = db.Column(db.String(100))
    Abstract = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Talk {self.name} {self.title}>'
    
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    IdPerson = (db.Integer)
    Name = db.Column(db.String(100), nullable=False)
    Institution = db.Column(db.String(100))
    def __repr__(self):
        return f'<Participant {self.name}>'
    
    
class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), primary_key=True, nullable=False)
    password = db.Column(db.String(100))
    trip = db.Column(db.Integer)
    dinner = db.Column(db.Integer)
    def __repr__(self):
        return f'<User {self.username}>'