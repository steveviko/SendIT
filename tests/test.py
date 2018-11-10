import unittest
from flask import request, jsonify, make_response,json
from app.models import Order
from app.views import app

class TestsOrder(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.order = Order()        
        self.sample_order= {          
            'item' :'Tv',
            'description':'LG',
            'destination':'Kampala',           
            'quantity':1
        }
        
    def test_order_creation(self):        
        self.assertIsInstance(self.order, Order)

    def test_add_order_method(self):
        self.assertEqual(len(self.order.delivery_orders),0)               
        response = self.app.post("/api/v1/parcels", data = json.dumps(self.sample_order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Order", response.data)
        
    def test_get_all_orders(self):
        response = self.app.get("/api/v1/parcels")
        self.assertEqual(response.status_code, 200)

    
    def test_fetch_an_order(self):
        response = self.app.get("/api/v1/parcels/1")
        self.assertEqual(response.status_code, 200)

    def test_cancel_order(self):       
        response = self.app.put("/api/v1/parcels/1/cancel", data = json.dumps(dict(item="watch",
                                                            description="rolex",
                                                            destination="kigali",
                                                            quantity=2, 
                                                            status="cancel")), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    #check whether order status is cancel
    def test_status_is_cancel(self):
        response = self.app.put('/api/v1/parcels/1/cancel',
                          content_type='application/json', 
                                data=json.dumps({"status": "cancel"})
                                )
        self.assertEqual(response.status_code, 200)  

    def test_user_id_type_input_returns_interger(self):        
        self.num =self.order.get_user_orders(2)
        self.assertIsInstance(self.num, int)

       
  