from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from flask_mail import Message

from flaskblog.extensions import mail
from flaskblog.models import User
from flaskblog.user.forms import LoginForm


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login', methods=["GET", "POST"])
def login_route():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).one()
		login_user(user)

		flash("Logged in successfully.", "success")
		return redirect(request.args.get("next") or url_for(".home_route"))

	return render_template('login.html', form=form)

@user_blueprint.route('/logout')
def logout_route():
	logout_user()
	flash("You have been logged out.", "success")

	return redirect(url_for(".home_route"))