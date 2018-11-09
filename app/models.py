from flask import jsonify, request,json
class Order:   
    delivery_orders = []

    def __init__(self):
        self.delivery_orders = []
        

    def add_order(self, item,description,destination, quantity):
        #check if item exist then update the quantity 
        request_data=request.data
        result  =json.loads(request_data)
        orders_numbers = 1
        for i in range(len(self.delivery_orders)):
            orders_numbers += 1
        result['order_id'] = orders_numbers
        result['user_id'] = orders_numbers
        orders= [order for order in self.delivery_orders if order['item'] == item]
        if not orders:
            new_order = {
                "order_id": int(orders_numbers), 
                "user_id": int(orders_numbers),               
                "item": item,
                "description": description,
                "destination":destination,
                "status": "Pending",
                "quantity":quantity
            }
            self.delivery_orders.append(new_order)
            return new_order
        else:
            orders[0]['quantity'] += quantity
            orders_numbers
            return orders
    
   
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

        user_order =[order for order in self.delivery_orders if order['user_id'] == userId]
        if user_order: 

            return user_order
           

        else:   
            return "No orders for this user"          
            

               
         
        
        
        