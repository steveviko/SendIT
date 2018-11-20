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

    