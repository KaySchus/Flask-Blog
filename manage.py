import os
import sys
import contextlib

from getpass import getpass

from flask_script import Manager, Server

from flaskblog import create_app
from flaskblog.models import db, User


env = os.environ.get('FLASKBLOG_ENV', 'dev')
app = create_app('flaskblog.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())

@manager.command
def create_db():
	db.create_all()

@manager.command
def drop_db():
	#Drops all DB tables
	db.drop_all()

@manager.command
def createuser():
	db.create_all()

	print('Enter username: ')
	username = input()
	print('Enter email address: ')
	email = input()
	password = getpass()
	assert password == getpass('Password (again):')

	user = User(username, email, password)
	db.session.add(user)
	db.session.commit()
	print('User added.')

if __name__ == "__main__":
    manager.run()