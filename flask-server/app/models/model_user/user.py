from app import db


class Guest(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

class User(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    pwd = db.Column(db.String(50),  nullable=False)

    def __init__(self, id=None, fname=None, lname=None, email=None, phone_number=None, username=None, pwd=None):
        self.id = None
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.pwd = pwd
