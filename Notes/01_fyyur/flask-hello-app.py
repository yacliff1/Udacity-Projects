from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Connecting to database | postgresql will automatically default to psycopg2 DBAPI
#Can also add + sign. Ex. 'postgresql+psycopg2://username... 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username@localhost:5432/databasename'
db = SQLAlchemy(app)

#Ex Person class with db.Model
#By default, SQL will set table equal to lowercase version of class. Use __tablename__ to specify name
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

#Detects models and creates tables for them
db.create_all()

@app.route('/')
def index():
    return 'Hello world!'