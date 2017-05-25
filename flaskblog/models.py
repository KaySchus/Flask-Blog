from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	confirmed_at = db.Column(db.DateTime())

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.set_password(password)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, value):
		return check_password_hash(password)

	@property
	def is_authenticated(self):
		if isinstance(self, AnonymousUserMixin):
			return False
		else:
			return True

	def is_active(self):
		return self.active

	def is_anonymous(self):
		if isinstance(self, AnonymousUserMixin):
			return True
		else:
			return False

	def get_confirmed_at(self):
		return self.confirmed_at

	def get_id(self):
		return self.id

	def __repr__(self):
		return '<User %r>' % self.username