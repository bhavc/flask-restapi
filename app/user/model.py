from sqlalchemy import Integer, Column, String
from app import db

class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    email = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

   
