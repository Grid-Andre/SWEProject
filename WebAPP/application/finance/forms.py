from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, ValidationError, DecimalField
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .models import Finance

class AddUserAccountForm(FlaskForm):
    AccountType = StringField('AccountType: ', [validators.DataRequired()])
    transaction = DecimalField('Balance: ', [validators.DataRequired()])
    Add = SubmitField('Add')


class Account(FlaskForm):
    Account = StringField('AccountType: ', [validators.DataRequired()])
    Add = SubmitField('Add')
