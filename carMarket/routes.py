from carMarket import app, db
from flask import render_template,redirect,url_for,flash,request
from carMarket.forms import RegisterForm, LoginAdmin, LoginForm, PurchaseForm, RegisterItem
from carMarket.models import Item,User,Admin
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
	return render_template('home.html')

@app.route("/market", methods=['GET','POST'])
@login_required
def market_place():
	purchase_form = PurchaseForm()

	if request.method == 'POST':
		purchased_item = request.form.get('purchased_item')
		p_item_object = Item.query.filter_by(barcode=purchased_item).first()
		if p_item_object:
			p_item_object.owner = current_user.id
			db.session.commit()
		return redirect(url_for('market_place'))

	if request.method == 'GET':
		items = Item.query.filter_by(owner=None)
		owned_items = Item.query.filter_by(owner=current_user.id)
		return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items)

@app.route("/register", methods=['GET','POST'])
def register_page():
	form = RegisterForm()

	#if form.errors != {}:
		#for err_msg in form.errors.values():
			#flash(f'There was an error creating a user: {err_msg}', category='danger')

	if form.validate_on_submit():
		if (form.first_name.data != "") and (form.last_name.data != "") and (form.email.data != "") and (form.password1.data != "") and ("@" in form.email.data):
			try:
				user_to_create = User(first_name=form.first_name.data,
				last_name=form.last_name.data,
				email=form.email.data,
				password=form.password1.data)

				db.session.add(user_to_create)
				db.session.commit()
				
				login_user(user_to_create)
				return redirect(url_for('market_place'))
			except IntegrityError:
				db.session.rollback()
		else:
			return redirect(url_for('register_page'))

	return render_template('register.html', form=form)


@app.route("/login", methods=["GET","POST"])
def login_page():
	form = LoginForm()
	attempted_user = User.query.filter_by(email=form.email.data).first()
	userStatus = User.query.filter_by(email=form.email.data,
		password=form.pass_word.data).first()
	if userStatus == None:
		pass
	else:
		login_user(attempted_user)
		return redirect(url_for('market_place'))
	return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
	logout_user()
	return redirect(url_for('home_page'))


@app.route("/myadmin", methods=["GET", "POST"])
def login_admin_page():
	logout_user()
	admForm = LoginAdmin()
	if admForm.validate_on_submit():
		userStatus = Admin.query.filter_by(username=admForm.user_name.data,
			password=admForm.pass_word.data).first()
		if userStatus == None:
			pass
		else:
			return redirect(url_for('admin_page'))
	return render_template('admlogin.html', admForm=admForm)


@app.route("/mlt-admin", methods=['GET','POST'])
def admin_page():
	form = RegisterItem()
	items = Item.query.filter_by(owner=None)
	all_items = Item.query.all()
	users = User.query.all()

	item_len = 0
	for item in items:
		item_len += 1

	owners_list = []
	for item in all_items:
		owners_list.append(item.owner)
	rank = {}
	for vls in owners_list:
		if vls in rank.keys():
			rank[vls] += 1
		else:
			rank[vls] = 1

	high_score = max(list(rank.values()))
	highest=list(rank.keys())[list(rank.values()).index(high_score)]

	highest_user = User.query.filter_by(id=highest).first()
	user_len = len(users)
	owned_item_len = len(all_items)-item_len

	if form.validate_on_submit():
		if (form.model.data != "") and (form.barcode.data != "") and (form.description.data != "") and (form.price.data != ""):
			try:
				item_to_create = Item(model=form.model.data,
				barcode=form.barcode.data,
				description=form.description.data,
				price=int(form.price.data))

				db.session.add(item_to_create)
				db.session.commit()
				
				return redirect(url_for('admin_page'))
			except IntegrityError:
				db.session.rollback()
		else:
			return redirect(url_for('admin_page'))

	return render_template('admin.html', items=items, all_items=all_items, users=users,
	 user_len=user_len, item_len=item_len, owned_item_len=owned_item_len, highest_user=highest_user,
	 form=form, high_score=high_score)
###learn decorators in python