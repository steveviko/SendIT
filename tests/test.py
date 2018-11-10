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
            'item' :'phone',
            'description':'sumsung',
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

    
       
  