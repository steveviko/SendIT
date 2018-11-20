# from app.views import app
from .user import User
from .dboperations import DbOperations
from .parcels import Parcels
from werkzeug.security import generate_password_hash, check_password_hash

userObject = User()
parcelObject = Parcels()

class UserActions:
    def __init__(self):
        self.db_Object = DbOperations()
        

    def user_register(self,email, password):
        
        userObject.email = email
        userObject.password = password
        hash_password = generate_password_hash(
            userObject.password, method='sha256')
      
        self.db_Object.register_user(
            userObject.email, userObject.password, hash_password
        )
        return {'message': 'user sucessfully created'}

    def add_user(self,account):
        """ insert a new user into the users table """
        command = "INSERT INTO users(username, email, password, role) VALUES(\
                '{}',  '{}', '{}', 'user')".format(account["username"],  account["email"]\
                , generate_password_hash(account["password"]))
        cursor.execute(command)
        return account

    def check_username(self, account):
        command = "SELECT username,password,role from users WHERE username= '{}'".format(account["username"])
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data