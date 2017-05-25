import os

from flask_script import Manager, Server

from flaskblog import create_app
from flaskblog.models import db, User


env = os.environ.get('FLASKBLOG_ENV', 'dev')
app = create_app('flaskblog.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())

@manager.command
def createdb():
	db.create_all()

if __name__ == "__main__":
    manager.run()