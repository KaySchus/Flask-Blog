from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Defining connection between User and Role
roles_users = db.Table('roles_users',
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	confirmed_at = db.Column(db.DateTime())
	roles = db.relationship('Role', secondary=roles_users,
		backref=db.backref('users', lazy='dynamic'))

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


# Creates datastore for adding Users to Roles with Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)