from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from flaskblog import assets

from flaskblog.extensions import assets_env

def create_app(object_name):
	"""
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
    """
	app = Flask(__name__)
	app.config.from_object(object_name)

    # Import and register the different assets bundles
	assets_loader = PythonAssetsLoader(assets)
	for name, bundle in assets_loader.load_bundles().items():
			assets_env.register(name, bundle)

	return app