from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields import DecimalField
from wtforms.validators import DataRequired, url

class ItemForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description')
    price = DecimalField('price', validators=[DataRequired()])