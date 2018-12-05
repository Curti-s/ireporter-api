#!/usr/bin/python
import os
from configparser import ConfigParser 

postgres_local_base = 'postgresql:///'
database_name = 'ireporter_api'
        

class Config(object):
    """Parent configuration class"""
    DEBUG = False
    CRSF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    DATABASE_URL = postgres_local_base + database_name

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = postgres_local_base + database_name + '_test'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    DATABASE_URL = postgres_local_base + database_name

app_config = {
    'development':DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

def db_config():
    with open('db.ini','r') as f:
        parser = ConfigParser()
        parser.read(f)
        db = dict()
        if parser.has_section('postgresql'):
            params = parser.items('postgresql')
            for param in params:
                db[param[0]] = param[1]
        return db