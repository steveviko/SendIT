from flask import jsonify, request,json

class User:
    """
    Creates a user object for each order.
    """
    def __init__(self,username,user_id):
        self.username = username
        self.user_id = user_id
class parcel:
    """
    Creates a parcel object for each order.
    """
    def __init__(self,ParcelId,item,description,destination,quantity):
        self.item = item
        self.description = description
        self.destination = destination
        self.parcelid = ParcelId
        self.status = "Pending"

        
        
        