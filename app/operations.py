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
    
    