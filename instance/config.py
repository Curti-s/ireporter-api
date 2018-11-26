import os

class Config(object):
    """Parent configuration class"""
    DEBUG = False
    CRSF_ENABLED = True
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

app_config = {
    'development':DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}