import os

class Config:

    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True    
    DEBUG = True
    

class TestConfig(Config):   
    TESTING = True
   
    