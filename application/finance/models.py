from application import db
from application import app
from datetime import datetime

class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    AccountType = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), db.ForeignKey('user.name'), nullable=False)
    transaction = db.Column(db.Float)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return '<Finance %r>' % self.AccountType


db.create_all()