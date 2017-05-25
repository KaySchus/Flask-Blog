class Config(object):
    # Secret key for session variables, will be used later
    SECRET_KEY = 'SUPER SECRET'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

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