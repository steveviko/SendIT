import os
class Config:

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True
    TESTNG = True
    DATABASE_URL = os.environ.get('DATABASE_URL')

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = os.environ.get('DATABASE_URL')