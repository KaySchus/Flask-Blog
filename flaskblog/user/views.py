from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from flask_mail import Message

from flaskblog.extensions import mail
from flaskblog.models import User, db
from flaskblog.user.forms import LoginForm, RegisterForm, ChangePasswordForm


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register', methods=["GET", "POST"])
def register_route():
	form = RegisterForm(request.form)

	if form.validate_on_submit():
		user = User(form.username.data, form.email.data, form.password.data)
		db.session.add(user)
		db.session.commit()

		print("Registered!")

		login_user(user)
		flash('You registed and are now logged in. Welcome!', 'success')
		return redirect(url_for("main.home_route"))

	return render_template('user/register.html', form=form)	


@user_blueprint.route('/login', methods=["GET", "POST"])
def login_route():
	form = LoginForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).one()
		login_user(user)

		flash("Logged in successfully.", "success")
		return redirect(request.args.get("next") or url_for("main.home_route"))

	return render_template('user/login.html', form=form)

@user_blueprint.route('/logout')
def logout_route():
	logout_user()
	flash("You have been logged out.", "success")

	return redirect(url_for("main.home_route"))

@user_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_route():
	form = ChangePasswordForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(email=current_user.email).first()
		if user:
			user.setpassword(form.password.data)
			db.session.commit()
			flash('Password successfully changed.', 'success')
			return redirect(url_for('user.profile_route'))
		else:
			flash('Password change was unsuccessful.', 'danger')
			return redirect(url_for('user.profile_route'))
			
	return render_template('user/profile.html', form=form)