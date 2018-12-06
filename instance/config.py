#!/usr/bin/python
import os
from configparser import ConfigParser 

class Config(object):
    """Parent configuration class"""
    DEBUG = False
    CRSF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL_TEST')

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL')

app_config = {
    'development':DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}