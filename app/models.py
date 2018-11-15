from flask import jsonify, request,json

class User:
    """
    Creates a user object for each order.
    """
    def __init__(self):
        self.username =None
        self.user_id = None 
        self.password = None

   


class parcel:
    """
    Creates a parcel object for each order.
    """
    def __init__(self):
        self.item = None
        self.description = None
        self.destination = None
        self.parcelid = None
        self.status = "Pending"

        