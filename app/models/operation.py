from app import db

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    records = db.relationship('Record', back_populates='operation')
