from flask import Flask, url_for, redirect, render_template, flash, request
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import ItemForm


basedir = os.path.abspath(os.path.dirname(__file__))



item_catalog = Flask(__name__)
item_catalog.config['SECRET_KEY'] = "b'c(\x18\xa3\xed,\xc4z\x9a7\x0c\x055\x15\xc2\xe5j\x9c\xd9w<\x90\xa7\x80'"
item_catalog.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'item_catalog.db')
db = SQLAlchemy(item_catalog)

import models

items = []

def store_item(title, description, price):
    items.append(dict(
        title = title,
        description = description,
        price = price,
        user = 'Louis',
        date = datetime.utcnow()
    ))




""" 
    ====================
          VIEWS
    ====================

"""

#index
@item_catalog.route('/')
@item_catalog.route('/index')
def index():
    return render_template('index.html', new_items=models.Item.newest(10))

#add
@item_catalog.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        price = form.price.data
        item = models.Item(title=title, description=description, price=price)
        db.session.add(item)
        db.session.commit()
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add_item.html', form=form)

#sign up
@item_catalog.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

#sign in
@item_catalog.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


"""
    ====================
          HTTP ERRORS
    ====================

"""
@item_catalog.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@item_catalog.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


def main():
    """main module"""
    pass


if __name__ == '__main__':
    item_catalog.run(debug=True)