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
            


@app.route('/api/v1/login', methods=['GET'])
def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('unauthorized accessss', 401, {'WWW-Authenticate':
                                                            'Basic realm="Login required!"'})
    user = user_obj.login_user(auth.username)
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate':
                                                     'Basic realm="Login required!"'})
   
    
    if check_password_hash(user['password'], auth.password):
        token = jwt.encode(
            {
                'user_id': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(
                    hours=48
                )
            }, app.config['SECRET_KEY']
        )
        return jsonify({'token': token.decode('UTF-8')}), 200
    return make_response('unauthorized access', 401, {'WWW-Authenticate':
                                                      'Basic realm="Login required!"'})


   






@app.route("/api/v1/users", methods=["GET"])
def fetch_all_users():
    new_users_lists=user_obj.fetch_all_users()
  
    return jsonify({"Users":new_users_lists}), 200

@app.route("/api/v1/parcels/<int:parcelId>", methods = ["GET"])
def get_an_order(parcelId):
    single_order = order_obj.Fetch_an_order(parcelId)
    if single_order:        
        return jsonify({"order": single_order}),200
    else:
        return jsonify({"Error": "Sorry you have entered incorrect  id"}), 400


@app.route("/api/v1/parcels", methods = ["GET"])
def Fetch_all_orders():
    orders = order_obj.Get_all_orders()
    if len(orders) =="":
        return jsonify({"order": "No orders available for delivery"}), 204   
    return jsonify({'orders': orders}), 200

@app.route('/api/v1/parcels/<parcelId>/cancel', methods=['PUT'])
def put_order(parcelId):    
    #cancel order on pending lists.
   
    data=request.data
    result  =json.loads(data) 
    order_status = result['status']
    
    if order_status not in ['Pending','cancel']:
        return jsonify({"message":"Error. Invalid  status"}), 400
    else:
        order= order_obj.cancel_order(int(parcelId), order_status)        
        return jsonify({"message":"Order cancelled successfully", "parcelList":order}), 200


@app.route("/api/v1/users/<int:user_id>/parcels", methods = ["GET"])
def Fetch_user_orders(user_id):
    user_orders = order_obj.get_user_order(user_id)
    if user_orders:        
        return jsonify({"orders": user_orders}),200
    else:
        return jsonify({"Error": "Sorry you have  incorrect user id"}), 400