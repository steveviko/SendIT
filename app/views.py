from flask import request, jsonify, make_response,json
from app import create_app

from app.models import Order

order_obj = Order()

app = create_app()

@app.route("/api/v1/parcels", methods=["POST"])
def post_order():
    #Add new order
    # try:
        request_data=request.data
        result  =json.loads(request_data)
        # result = request.get_json() 
        new_order = {                             
                "item": result["item"],
                "description": result["description"],
                "destination":result["destination"],                
                "quantity":result["quantity"]
            }
    
        if  new_order:
            order_obj.add_order(new_order)
            return jsonify({"Parcels": new_order}), 201
        
        
  

@app.route("/api/v1/parcels/<int:parcelId>", methods = ["GET"])
def get_an_order(parcelId):
    single_order = order_obj.Fetch_an_order(parcelId)
    if single_order:        
        return jsonify({"order": single_order}),200
    else:
        return jsonify({"Error": "Sorry you have entered incorrect  id"}), 400


@app.route("/api/v1/parcels", methods = ["GET"])
def Fetch_all_orders():
    orders = order_obj.get_all_orders()
    if len(orders) ==[]:
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
        cancelled_order= order_obj.Cancel_order(int(parcelId),order_status)        
        return jsonify({"Cancelled order": cancelled_order}), 200

@app.route("/api/v1/users/<int:userId>/parcels", methods = ["GET"])
def Fetch_user_orders(userId):
    user_orders = order_obj.get_user_orders(userId)
    if user_orders:        
        return jsonify({"orders": user_orders}),200
    else:
        return jsonify({"Error": "Sorry you have  incorrect user id"}), 400