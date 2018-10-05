from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields import DecimalField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, url


class ItemForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description')
    price = DecimalField('price', validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')