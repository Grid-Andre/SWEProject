from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, ValidationError, DecimalField, IntegerField, SelectField
from flask_wtf.file import FileRequired,FileAllowed, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm
from .models import Fitness


class Cal(FlaskForm):
    Weight = DecimalField('Weight (lbs)', [validators.DataRequired()])
    DurationHR = IntegerField('DurationHR (Hr)')
    DurationMin = IntegerField('DurationMin (min/s)', [validators.DataRequired()])
    ExerciseType = StringField('ExerciseType', [validators.DataRequired()])
    Add = SubmitField('Add')


