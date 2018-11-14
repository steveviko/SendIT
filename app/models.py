import uuid
import random
from flask import jsonify, request,json
class Order:   
    

    def __init__(self):
        self.delivery_orders = []
        

    def add_order(self, new_order):
        new_order["order_id"] = int(uuid.uuid4())
        new_order["user_id"] = int(uuid.uuid4())
        new_order["order_status"] = "Pending"
        self.delivery_orders.append(new_order)
        return new_order
        
            
        
    def Fetch_an_order(self, parcelId):
        for order in self.delivery_orders:
            if order["order_id"] == parcelId: 
                return order

    def get_all_orders(self):
        #Return list of all orders      
        return self.delivery_orders

    def Cancel_order(self, parcelId,order_status):        
        #method to Cancel specific order using the id. 
        Parcel_data = [order for order in self.delivery_orders if order['order_id'] == parcelId]
        if not Parcel_data:
            return "does not exist"                
  
            
        else:
            data=request.data
            result  =json.loads(data) 
            Parcel_data[0]['status'] =result['status']
            return Parcel_data[0]
            
            
    def get_user_orders(self, userId):
        number_types = (int, float, complex)
 
        if isinstance(userId, number_types):
            return userId 
        else:
            raise ValueError

        user_order =[order for order in self.delivery_orders if order['user_id'] == userId]
        if user_order: 

            return user_order
           

        else:   
            return "No orders for this user"          
            

               
         
        
        
        