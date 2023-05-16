from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    
    records = db.relationship('Record', back_populates='user')
