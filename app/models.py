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
        orders= [order for order in self.delivery_orders if order['item'] == item]
        if not orders:
            new_order = {
                "order_id": int(orders_numbers),                
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
    
   
            