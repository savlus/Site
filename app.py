from flask import Flask
from flask_sqlalchemy import SQLAlchemy
site = Flask(__name__)
site.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
site.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(site)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    second_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)