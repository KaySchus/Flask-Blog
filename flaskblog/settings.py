class Config(object):
    # Secret key for session variables, will be used later
    SECRET_KEY = 'REPLACE ME - NOT USED YET'

# Production Configuration
class ProdConfig(Config):
    ENV = 'prod'

# Development Configuration
class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    ASSETS_DEBUG = True

# Configuration for conducting tests
class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    WTF_CSRF_ENABLED = False