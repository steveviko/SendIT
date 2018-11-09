from flask import request, jsonify, make_response,json
from app import app
from app.models import Order

order_obj = Order()

@app.route("/api/v1/parcels", methods=["POST"])
def post_order():
    #Add new order
    try:
        request_data=request.data
        result  =json.loads(request_data)
        # result = request.get_json() 
        
        verify_order = order_obj.add_order(result['item'], 
                                            result['description'],
                                            result['destination'],
                                            result['quantity'])
        
    except Exception as err:
        return jsonify({"Message": "Please add the {}  field".format(str(err))}), 400

    if result['description'] is None or type(result['description']) != str or result['description'] is "" :
        return jsonify({"Message":"Description should be text"}), 400

    else:
        return jsonify({"Order": verify_order}), 201

