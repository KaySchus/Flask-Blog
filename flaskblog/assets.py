from flask_assets import Bundle

common_css = Bundle(
	'css/vendor/pure-min.css',
	'css/vendor/grids-responsive-min.css',
	'css/sidebar.css',
	filters='cssmin',
	output='public/css/common.css'
)