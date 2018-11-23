import os

class Config:

    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True    
    DEBUG = True
    DB_NAME = "test_sendit"
    DB_USER = "postgres"
    DB_PASS = "password"
    DB_HOST = "localhost"

class TestConfig(Config):   
    TESTING = True
   
    DB_NAME = "test_sendit"
    DB_USER = "postgres"
    DB_PASS = "password"
    DB_HOST = "localhost"