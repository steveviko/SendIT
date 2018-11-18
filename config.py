import os
class BaseConfig:

    DEBUG = False

class DevelopmentConfig(BaseConfig):

    DEBUG = True
    TESTNG = True
    

class TestConfig(BaseConfig):
   
    TESTING = True
   
