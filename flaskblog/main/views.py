from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from flask_mail import Message

from flaskblog.extensions import mail
from flaskblog.models import User


main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home_route():
	return render_template('index.html')