# the data that will be used in database will be represented by collection
# of classes , usually called database models

from app import database
from app import login
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class User(UserMixin, database.Model):
    # UserMixin prepares the User Model for flask-login
    __tablename__="user"
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(64), index=True, unique=True)
    email = database.Column(database.String(120), index=True, unique=True)
    password_hash = database.Column(database.String(128))
    posts = database.relationship('Posts', backref='author', lazy=True)
    # backref is a simple way to declare a new porperty to the post class
    # lazy defines when sql will load the data from the database 
    # lazy = True means that SQLAlchemy will load the data as necessary 
    # using the standard select comand

    def set_password(self, password):
        # this method implements password hashing 
        self.password_hash=generate_password_hash(password)

    def check_password(self, password):
        # chech the password stored in database 
        return check_password_hash(self.password_hash,password)



class Posts(database.Model):
    __tablename__ ="posts"
    id = database.Column(database.Integer, primary_key=True)
    body = database.Column(database.String(140))
    timestamp = database.Column(database.DateTime, index=True, default=datetime.utcnow)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    #flask-login keeps track of the logged in user by storing its id 
    # in flasks user session. A storage space assigned to each user who 
    # connects to the application. Because flask login does not anything 
    # the database it needs application helps in loading the user
    # for that reason the extention expects the application will configure
    # a user loaderfuncion and then can be called to load a user with the given id
    return User.query.get(int(id))






