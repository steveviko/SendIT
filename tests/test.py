import unittest
from flask import request, jsonify, make_response,json
from app.models import parcel,User
from app.operations import Orders,UserActions
from app.views import app

class TestsOrder(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.order = Orders()  
        self.user = User()      
        self.sample_order= {          
            'item' :'Tv',
            'description':'LG',
            'destination':'Kampala',           
            'status':'pending'
        }
        
    def test_order_creation(self):        
        self.assertIsInstance(self.order, Orders)

    def test_user_obj_creation(self):        
        self.assertIsInstance(self.user, User)

    def test_add_order_method(self):
        self.assertEqual(len(self.order.parcel_lists),0) 
        self.order.add_orders(self.sample_order)
        self.assertEqual(len(self.order.parcel_lists),1)             
        response = self.app.post("/api/v1/parcels", data = json.dumps(self.sample_order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        
        
    # def test_get_all_orders(self):
    #     response = self.app.get("/api/v1/parcels")
    #     self.assertEqual(response.status_code, 200)

    
    # def test_fetch_an_order(self):
    #     response = self.app.get("/api/v1/parcels/1")
    #     self.assertEqual(response.status_code, 200)

    # def test_cancel_order(self):       
    #     response = self.app.put("/api/v1/parcels/1/cancel", data = json.dumps(dict(item="watch",
    #                                                         description="rolex",
    #                                                         destination="kigali",
    #                                                         quantity=2, 
    #                                                         status="cancel")), content_type = 'application/json')
    #     self.assertEqual(response.status_code, 200)

    # #check whether order status is cancel
    # def test_status_is_cancel(self):
    #     response = self.app.put('/api/v1/parcels/1/cancel',
    #                       content_type='application/json', 
    #                             data=json.dumps({"status": "cancel"})
    #                             )
    #     self.assertEqual(response.status_code, 200)  

    # def test_user_id_type_input_returns_interger(self):        
    #     self.num =self.order.get_user_order(2)
    #     self.assertIsInstance(self.num, int)

       
  