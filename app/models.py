class Order:   
    delivery_orders = []

    def __init__(self):
        self.delivery_orders = []
        self.order_id = 1        
        self.item = ''
        self.description ='' 
        self.destination=''      
        self.quantity = 0

    def add_order(self, item,description,destination, quantity):
        #check if item exist then update the quantity 
        orders= [
            order for order in self.delivery_orders if order['item'] == item]
        if not orders:
            new_order = {
                "order_id": self.order_id,                
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

            self.order_id += 1
            return orders
    
