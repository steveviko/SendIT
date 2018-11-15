from flask import request, jsonify,make_response, redirect, json, Response, request, abort
from app import create_app
import jwt
from werkzeug.security import check_password_hash
import datetime
from app.operations import Orders,UserActions



order_obj = Orders()
user_obj =UserActions()


app = create_app()
app.config['SECRET_KEY'] = 'usersecret'

@app.route("/api/v1/parcels", methods=["POST"])
def create_order():
    if request.method == 'POST':

        #data from the user  
        result = request.data
        data=json.loads(result)

        # empty json request

        if not data:
            return jsonify({"error":"Invalid inputs"}), 400
        else:
            order = {
                        "item": data["item"],
                        "description": data["description"],
                        "destination": data["destination"]
                        
                        # "username": data["username"]                        
                    }
          
            parcel =order_obj.add_orders(order)          
            return jsonify({"ParcelList":parcel}), 201
        
