from app import db
from datetime import datetime

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.String(255), nullable=False)
    user_balance = db.Column(db.Float, nullable=False)
    operation_response = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)

    # Relationship fields
    user = db.relationship('User', back_populates='records')
    operation = db.relationship('Operation', back_populates='records')
    
    def to_dict(self):
        return {
            'id': self.id,
            'operation_id': self.operation_id,
            'amount': self.amount,
            'user_balance': self.user_balance,
            'operation_response': self.operation_response,
        }