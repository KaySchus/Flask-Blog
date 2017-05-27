from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators
from wtforms.validators import DataRequired, Email, Length,EqualTo

from flaskblog.models import User


# Temporary until I devise a better solution
U_MIN_LENGTH = 4
U_MAX_LENGTH = 40

P_MIN_LENGTH = 6
P_MAX_LENGTH = 40

E_MIN_LENGTH = 6
E_MAX_LENGTH = 254


class LoginForm(FlaskForm):
	username = TextField(u'Username', validators=[validators.required()])
	password = PasswordField(u'Password', validators=[validators.optional()])

	def validate(self):
		check_validate = super(LoginForm, self).validate()

		# If the above validators fail
		if not check_validate:
			return False

		# Does our user exist (Checks both username OR password - kind of dirty)
		user = User.query.filter_by(username=self.username.data).first()
		if not user:
			self.username.errors.append('Invalid username or password')
			return False

		# Do the passwords match
		if not user.check_password(self.password.data):
			self.username.errors.append('Invalid username or password')
			return False

		return True

class RegisterForm(FlaskForm):
	username = TextField(
		u'Username',
		validators=[DataRequired(), Length(min=U_MIN_LENGTH, max=U_MAX_LENGTH)]
	)

	email = TextField(
		u'Email',
		validators=[DataRequired(), Email(message=None), Length(min=E_MIN_LENGTH, max=E_MAX_LENGTH)]
	)

	password = PasswordField(
		u'Password',
		validators=[DataRequired(), Length(min=P_MIN_LENGTH, max=P_MAX_LENGTH)]
	)

	confirm = PasswordField(
		u'Repeat password',
		validators=[
			DataRequired(),
			EqualTo('password', message='Passwords must match.')
		]
	)

	def validate(self):
		initial_validation = super(RegisterForm, self).validate()
		if not initial_validation:
			return False

		user = User.query.filter_by(username=self.username.data).first()
		if user:
			self.username.errors.append("Username already in use")
			return False

		user = User.query.filter_by(email=self.email.data).first()
		if user:
			self.email.errors.append("Email already registered")
			return False

		return True

class ChangePasswordForm(FlaskForm):
	password = PasswordField(
		u'Password',
		validators=[DataRequired(), Length(min=P_MIN_LENGTH, max=P_MAX_LENGTH)]
	)

	confirm = PasswordField(
		u'Repeat password',
		validators=[
			DataRequired(),
			EqualTo('password', message='Passwords must match.')
		]
	)