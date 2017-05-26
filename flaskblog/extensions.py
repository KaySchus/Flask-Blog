from flask_login import LoginManager
from flask_assets import Environment
from flask_mail import Mail

from flaskblog.models import User

# Init flask assets
assets_env = Environment()

login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"

mail = Mail()

@login_manager.user_loader
def load_user(userid):
	return User.query.get(userid)