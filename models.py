from datetime import datetime
from sqlalchemy import desc
from item_catalog import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))

    @staticmethod
    def newest(num):
        return Item.query.order_by(desc(Item.date)).limit(num)

    def __repr__(self):
        return "<Item '{}': '{}'>".format(self.description, self.title)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username