from flask import Flask, url_for, redirect, render_template, flash, request
from __init__ import app, db, login_manager
from forms import ItemForm, LoginForm
from models import User, Item
from flask_login import login_required, login_user, current_user, logout_user


# login manager
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


# Fake Login
def logged_in_user():
    return User.query.filter_by(username='magdaleno').first()


# index
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_items=Item.newest(10))


# add
@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        price = form.price.data
        item = Item(user=current_user, title=title, description=description, price=price)
        db.session.add(item)
        db.session.commit()
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add_item.html', form=form)


# sign up
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


# sign in
@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


# user
@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


# login
@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}.".format(user.username))
            return redirect(request.args.get('next') or url_for('user', username=user.username))
        flash('Incorrect username or password.')
    return render_template("login.html", form=form)


# logout
@app.route('/sign_out')
def sign_out():
    logout_user()
    return redirect(url_for('index'))

"""
    ====================
          HTTP ERRORS
    ====================

"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500