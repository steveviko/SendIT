import unittest
from flask import request, jsonify, make_response,json
from app.parcels import Parcels
from app.user import User
from app.dboperations import DbOperations
from app import create_app
from app.views import app

class TestDevelopmentConfig(unittest.TestCase):
    def create_app(self):
        app.config.from_object('app.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(create_app is None)
        self.assertTrue(
            app.config['DATABASE_URI'] == 'postgresql://postgres:password@localhost/test_sendit'
        )

class TestsOrder(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.Parcel = Parcels()  
        self.user = User() 
        # self.userAction =UserActions()     
        self.sample_order= {          
            'item' :'Tv',
            'description':'LG',
            'destination':'Kampala',           
            'status':'pending'
        }
        
    def test_order_creation(self):        
        self.assertIsInstance(self.Parcel, Parcels)

    def test_user_obj_creation(self):        
        self.assertIsInstance(self.user, User)

    # def test_add_order_method(self):
    #     self.assertEqual(len(self.order.parcel_lists),0) 
    #     self.order.add_orders(self.sample_order)
    #     self.assertEqual(len(self.order.parcel_lists),1)             

        response = self.app.post("/api/v1/parcels", data = json.dumps(self.sample_order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        
        
    def test_get_all_orders(self):
        response = self.app.get("/api/v1/parcels")
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

    
    
    # def test_user_register(self):
    #     username = "steve"
    #     password = "w123"
    #     assert self.userAction.register_user(username, password)
       
    # def test_user_login(self):
    #     username = "steve"
    #     assert self.userAction.login_user(username)
       