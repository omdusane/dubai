from utils import db

class Enquiries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=False)
    subject = db.Column(db.String(200), nullable=False,unique=False)
    message = db.Column(db.String(500), nullable=False, unique=False)

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=False)
    