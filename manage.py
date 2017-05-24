import os

from flask_script import Manager, Server
from flaskblog import create_app


env = os.environ.get('FLASKBLOG_ENV', 'dev')
app = create_app('flaskblog.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())

if __name__ == "__main__":
    manager.run()