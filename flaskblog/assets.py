from flask_assets import Bundle

common_css = Bundle(
	'css/vendor/pure.min.css',
	filters='cssmin',
)