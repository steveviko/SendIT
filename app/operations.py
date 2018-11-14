from app.models import User,parcel

class Order:   
    
    #initialize order and user lists
    def __init__(self):
        self.delivery_orders = []
        self.user_lists=[]

    
    
         