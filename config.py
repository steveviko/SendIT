import os
class BaseConfig:

    DEBUG = False

class DevelopmentConfig(BaseConfig):

    DEVELOPMENT = True
    TESTNG = True
    

class TestConfig(BaseConfig):
   
    TESTING = True
   
