from flask import render_template, Blueprint, session, request,redirect,url_for,flash
from application import app, db, bcrypt
from .forms import RegistrationForm, LoginForm


@app.route('/')
def home():
    return render_template('dashboard.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash(f'welcome {form.name.data} Thanks for registering','success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/register.html',title='Register user', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'welcome {form.email.data} you are logedin now','success')
            return redirect(url_for('admin'))
        else:
            flash(f'Wrong email and password', 'success')
            return redirect(url_for('login'))
    return render_template('admin/login.html',title='Login page',form=form)


from .models import User
