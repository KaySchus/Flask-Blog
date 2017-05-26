from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms import validators

from flaskblog.models import User


class LoginForm(FlaskForm):
	username = TextField(u'Username', validators=[validators.required()])
	password = PasswordField(u'Password', validators=[validators.optional()])

	def validate(self):
		check_validate = super(LoginForm, self).validate()

		# If the above validators fail
		if not check_validate:
			return False

		# Does our user exist
		user = User.query.filter_by(username=self.username.data).first()
		if not user:
			self.username.errors.append('Invalid username or password')
			return False

		# Do the passwords match
		if not user.check_password(self.password.data):
			self.username.errors.append('Invalid username or password')
			return False

		return True