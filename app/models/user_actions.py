# from app.views import app
from .user import User
from app.database.dboperations import DbOperations
from .parcels import Parcels
from werkzeug.security import generate_password_hash, check_password_hash

user_Obj = User()
parcelObject = Parcels()

class UserActions:
    def __init__(self):
        self.db_Object = DbOperations()
        

    # def user_login(self, username):
    #     user_obj.username = username
        
    #     get_user = self.db.Object.fetch_user_name(
    #         user_Obj.username
    #     )
    #     return get_user

    
    