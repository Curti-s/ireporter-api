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

app_config = {
    'development':DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

# database config
def dbconfig(filename='instance/database.ini',section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file 
    parser.read(filename)

    # get section, default to PostgreSQL
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in {1} file'.format(section,filename))

    return db
