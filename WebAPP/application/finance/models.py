from application import db
from application import app

class Finance(db.Model):
    FinanceID = db.Column(db.Integer, primary_key=True)
    CurrCash = db.Column(db.Numeric, unique=False, nullable=True)
    Salary = db.Column(db.Numeric, unique=False, nullable=True)

    def __repr__(self):
        return '<Finance %r>' % self.FinanceID


db.create_all()