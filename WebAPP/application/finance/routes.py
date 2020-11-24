from flask import render_template, Blueprint, session, request,redirect,url_for,flash
from application import app, db


@app.route('/account')
def account():
    return render_template('finance/accounts.html')

@app.route('/transactions')
def transactions():
    return render_template('finance/transactions.html')

@app.route('/balance')
def balance():
    return render_template('finance/balance.html')


from .models import Finance