from application import db
from application import app


class Fitness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ExerciseType = db.Column(db.String(50), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    #weight = db.Column(db.Integer)
    baseCal = db.Column(db.Integer, nullable=False)

    '''def __repr__(self):
         return '< %r>' % self.ExerciseType'''


db.create_all()