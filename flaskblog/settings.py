import os
import configparser

basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.abspath(os.path.join(basedir, os.pardir))
config_settings = configparser.ConfigParser()
config_settings.read(os.path.join(parentdir, 'config.ini'))

class Config(object):
    # Secret key for session variables, will be used later
    SECRET_KEY = 'SUPER SECRET'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SERVER = config_settings['Email']['MAIL_SERVER']
    MAIL_USERNAME = config_settings['Email']['MAIL_USERNAME']
    MAIL_PASSWORD = config_settings['Email']['MAIL_PASSWORD']

    SECRET_KEY = config_settings['Key']['SECRET_KEY']

# Production Configuration
class ProdConfig(Config):
    ENV = 'prod'

# Development Configuration
class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    ASSETS_DEBUG = True

# Configuration for conducting tests
class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    WTF_CSRF_ENABLED = False