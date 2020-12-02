from flask import render_template, Blueprint, session, request,redirect,url_for,flash
from flask_login import login_required, current_user, logout_user, login_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.sql import func
from .forms import AddUserAccountForm, Account
from application import app, db


@app.route('/account')
def account():
    return render_template('finance/accounts.html')

@app.route('/transactions')
def transactions():
    return render_template('finance/transactions.html')

@app.route('/balance', methods=['GET', 'POST'])
def showbalance():
    form = Account()
    if form.validate_on_submit():
        account = form.Account.data
    
    balance = Finance.query.with_entities(func.sum(Finance.transaction).label('sum')).filter_by(
            username=current_user.name,
            AccountType=form.Account.data
            ).order_by(Finance.transaction).all()

    return render_template('finance/balance.html', form=form, value=balance)

@app.route('/account/addaccount', methods=['GET', 'POST'])
def addaccount():
    form = AddUserAccountForm()
    if form.validate_on_submit():
        finance = Finance(AccountType=form.AccountType.data, username=current_user.name, transaction=form.transaction.data)
        try:
            db.session.add(finance)
            db.session.commit()
            flash('You successfully added your transaction.')
            return redirect(url_for('addaccount'))
        except exc.IntegrityError:
            return redirect(url_for('addaccount'))
              
    return render_template('finance/addaccount.html', form=form)



from .models import Finance


