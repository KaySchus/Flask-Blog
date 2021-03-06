from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from flaskblog import assets
from flaskblog.models import db
from flaskblog.main.views import main_blueprint
from flaskblog.user.views import user_blueprint

from flaskblog.extensions import (
	assets_env,
	login_manager,
	mail
)

def create_app(object_name):
	"""
	An flask application factory, as explained here:
	http://flask.pocoo.org/docs/patterns/appfactories/
	Arguments:
		object_name: the python path of the config object,
					 e.g. appname.settings.ProdConfig
	"""
	app = Flask(__name__, static_url_path='/static')
	app.config.from_object(object_name)

	db.init_app(app)

	login_manager.init_app(app)

	mail.init_app(app)

	# Import and register the different assets bundles
	assets_env.init_app(app)
	assets_loader = PythonAssetsLoader(assets)
	for name, bundle in assets_loader.load_bundles().items():
			assets_env.register(name, bundle)

	# Loading the Blueprint in controllers defined by main.py - Handles routing
	app.register_blueprint(main_blueprint)
	app.register_blueprint(user_blueprint)

	return app