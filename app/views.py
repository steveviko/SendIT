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
        
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        #data from the user  
        result = request.data
        data=json.loads(result)
        if not data:
            return jsonify({'error': 'unsupported Request'}), 400
        elif 'username' not in data:
            return jsonify({'error': 'username is requred'}), 400
        elif 'password' not in data:
            return jsonify({'error': 'password is required'}), 400
        username=data["username"]
        password=data['password']          

        if username=="" or password=="":
            return jsonify({"Error": "No user Found"}), 400
            
        else:
            user_obj.register_user(username, password)
            return jsonify({'Message': 'New user registered successfully' }), 201
            

@app.route("/api/v1/users", methods=["GET"])
def fetch_all_users():
    new_users_lists=user_obj.fetch_all_users()
  
    return jsonify({"Users":new_users_lists}), 200
