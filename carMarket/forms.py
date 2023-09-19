from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from carMarket.models import Admin
#from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):
    first_name = StringField(label='Firstname:')
    last_name = StringField(label='Lastname:')
    email = StringField(label='Email Address:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')

class LoginAdmin(FlaskForm):
	user_name = StringField(label='Username:')
	pass_word = PasswordField(label='Password:')
	submit = SubmitField(label='Enter Admin Page')

class LoginForm(FlaskForm):
	email = StringField(label='Username:')
	pass_word = PasswordField(label='Password:')
	submit = SubmitField(label='Log in')

class PurchaseForm(FlaskForm):
	submit = SubmitField(label='Purchase Car')

class RegisterItem(FlaskForm):
	model = StringField(label='Model:')
	barcode = StringField(label='Barcode:')
	description = TextAreaField(label='Description:')
	price = StringField(label='Price:')
	submit = SubmitField(label='Add to Market')