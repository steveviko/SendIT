import uuid
from app.models import User,parcel
from werkzeug.security import generate_password_hash, check_password_hash

user =User()
parcel =parcel()

class Orders:   
    
    #initialize parcel lists
    def __init__(self):
        self.parcel_lists = []
       
    def add_orders(self, order):
        order["parcelid"] = int(uuid.uuid4().clock_seq)
        order["status"] = "Pending"
        self.parcel_lists.append(order)
        return order
    
    def Get_all_orders(self):
        return self.parcel_lists




class UserActions:
     #initialize user lists
    def __init__(self):
        self.user_lists = []

    
    def register_user(self, username, password):
        user.username = username
        user.password = password
        hash_password = generate_password_hash(user.password, method='sha256')
        user.user_id= int(uuid.uuid4().clock_seq)
        new_user =[user.user_id,user.username, hash_password ]
        
        for users in new_user:
            user_data={}
            user_data["user_id"] = int(uuid.uuid4().clock_seq)
            user_data["username"] = username
            user_data["password"] = generate_password_hash(user.password, method='sha256')
           
        self.user_lists.append(user_data )
        return new_user

    def login_user(self, username):
        # user.username = username
        # current_user =self.user_lists.fetch_all_users(user.username)
        current_user =[users for users in self.user_lists if  users['username']== username]
        if not current_user:
            return {"Message": "No username  Found"}
        else:
            return current_user[0]

    def fetch_all_users(self):
        users = self.user_lists[:]
        return users 
