import os
class BaseConfig:

    DEBUG = False

class DevelopmentConfig(BaseConfig):

    DEVELOPMENT = True
    TESTNG = True
    DATABASE_URL = os.environ.get('DATABASE_URL')
    

class TestConfig(BaseConfig):

   
    TESTING = True
    DATABASE_URL = os.environ.get('DATABASE_URL')
   
