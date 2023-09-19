from carMarket import db, login_manager
#from carMarket import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

class Item(db.Model):
	model = db.Column(db.String(length=30), nullable=False)
	barcode = db.Column(db.String(length=9), nullable=False, unique= True, primary_key=True)
	description = db.Column(db.String(length=1024), nullable=False)
	price = db.Column(db.Integer(), nullable=False)
	owner = db.Column(db.String(length=50), db.ForeignKey('user.email'))

	def __repr__(self):
		return f"{self.model} {self.barcode}"

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	first_name = db.Column(db.String(length=20), nullable=False)
	last_name = db.Column(db.String(length=20), nullable=False)
	email = db.Column(db.String(length=50), nullable=False, unique=True)
	password = db.Column(db.String(length=9), nullable=False, unique=True)
	items = db.relationship('Item', backref='owned_user', lazy=True)

	def __repr__(self):
		return f"{self.id}, {self.email}, {self.password}"

	#@property
	#def password_(self):
		#return self.password_
	
	#@password_.setter
	#def password_(self, plain_text_password):
		#self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Admin(db.Model):
	username = db.Column(db.String(length=20), nullable=False)
	password = db.Column(db.String(length=9), nullable=False, unique=True, primary_key=True)

	def __repr__(self):
		return f"{self.username}, {self.password}"