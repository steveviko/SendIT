from flask import request, jsonify,make_response, redirect, json, Response, abort
from app import create_app
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from app.user_actions import UserActions
from app.validation import validator
from app.user import User
from app.dboperations import DbOperations

user_obj = UserActions()
validate = validator()
user = User()
db_obj = DbOperations()



app = create_app()
app.config['SECRET_KEY'] = 'usersecret'

        
@app.route('/api/v2/auth/signup', methods=['POST'])
def signup_user():
    if request.method == 'POST':
        #data from the user  
        result = request.data
        data=json.loads(result)
        if not data:
            return jsonify({'error': 'unsupported Request'}), 400
        elif 'username' not in data:
            return jsonify({'error': 'username is requred'}), 400
        elif 'email' not in data:
            return jsonify({'error': 'email is required'}), 400
        elif 'password' not in data:
            return jsonify({'error': 'password is required'}), 400
        elif 'role' not in data:
            return jsonify({'error': 'role is required'}), 400
        
        account = {
                "username": data["username"],
                "email": data["email"],
                "password": data["password"],
                "role": data["role"]
            }       
        empty_space = validate.validate_empty_space(account)
        if empty_space:
            return jsonify({"Error": "invalid input"}), 400
        None_username = db_obj.check_username(account)
        if not None_username:
            new_account = db_obj.add_user(account)
            return jsonify({'Message': 'New user registered successfully','user':new_account }), 201
        else:
            return jsonify({"Error": "user already exists"}), 409
            
        
    else:
        return jsonify({"Error": "Method Not allowed"})      





@app.route('/api/v2/login', methods=['POST'])
def login_user():
    auth = json.loads(request.data)
    
    if not auth or not auth['username'] or not auth['password']:
        return make_response('unauthorized accessss', 401, {'WWW-Authenticate':
                                                            'Basic realm="Login required!"'})
    user = db_obj.check_username(auth['username'])
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate':
                                                     'Basic realm="Login required!"'})
    # password = db_obj.check_username(auth.password,)
    
    if check_password_hash(user["hash_password"], auth['password']):
        # return str(user['user_id'])
        token = jwt.encode(
            {
                'user_id': user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(
                    hours=48
                )
            }, app.config['SECRET_KEY']
        )
        return jsonify({'token': token.decode('UTF-8')}), 200
    return make_response('unauthorized access', 401, {'WWW-Authenticate':
                                                      'Basic realm="Login required!"'})

@app.route('/api/v2/parcels', methods=['POST'])
def create_parcels():
    data =json.loads(request.data)
    if not data:
        return jsonify({'message': 'unsupported format'}), 400
    elif 'item' not in data:
        return jsonify({'message': 'item  is requred'}), 400
    elif 'description' not in data:
        return jsonify({'message': 'description  is required'}), 400
    elif 'destination' not in data:
        return jsonify({'message': 'destination  is required'}), 400
    elif 'current_location' not in data:
        return jsonify({'message': 'current_location  is required'}), 400
    # elif 'status' not in data:
    #     return jsonify({'message': 'status  is required'}), 400
    elif "item"=="" or "description"=="" or "destination"==""or "current_lcation"=="":
        return jsonify({'message': 'Fields in all required values'}), 400
    if data:
        parcel={
        "item" : data['item'],
        "description" :data['description'],
        "destination" :data['destination'],
        "current_location" :data['current_location']}
       

        new_parcel=db_obj.add_parcel(parcel,user_id=1)
        return jsonify({'message': 'parcel successfully created','parcel':new_parcel}), 201
    return 

@app.route("/api/v2/parcels", methods=["GET"])
def get_all_parcelss():
    """Implements the get all parcel delivery orders api."""   
    parcel_list = db_obj.get_parcels()
    return jsonify({'parcels': parcel_list}), 200

@app.route("/api/v2/parcels/<parcel_id>", methods=["GET"])

def get_single_parcel(parcel_id):
    """Implements api to get a specific parcel delivery order."""   

    parcel = db_obj.get_one_parcel(int(parcel_id))    
    return jsonify({"Parcel": parcel}), 200

  