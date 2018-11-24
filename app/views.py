from flask import request, jsonify,make_response, redirect, json, Response, abort
from app import create_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from functools import wraps
from app.models.user_actions import UserActions
from app.database.validation import validator
from app.models.user import User
from app.database.dboperations import DbOperations

user_obj = UserActions()
validate = validator()
user = User()
db_obj = DbOperations()



app = create_app()
app.config['SECRET_KEY'] = 'usersecret'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_use = db_obj.fetch_user_by_id(data['user_id'])
            current_user = current_use[0]
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route("/api/v1/users", methods=["GET"])
def fetch_all_users():
    users=db_obj.query_user()      
    return jsonify({"Users":users}), 200
        
@app.route('/api/v2/auth/signup', methods=['POST'])
def signup_user():
    
    result = request.data
    data=json.loads(result)        
    if not data:
        return jsonify({'error': 'unsupported Request'}), 400
    elif 'username' not in data:
        return jsonify({'error': 'username is requred'}), 400
    elif 'email' not in data:
        return jsonify({'error': 'email is required'}), 400        
    elif 'hash_password' not in data:
        return jsonify({'error': 'password is required'}), 400
    elif 'role' not in data:
        return jsonify({'error': 'role is required'}), 400
    # check_email =valid_email(data['email'])
    # if check_email:
    account = {
            "username": data["username"],
            "email": data["email"],
            "hash_password": data["hash_password"],
            "role": data["role"]
        }   
    
    empty_space = validate.validate_empty_space(account)
    if empty_space:
        return jsonify({"Error": "invalid input"}), 400
    None_username = db_obj.check_username(account)
    if not None_username:
        db_obj.add_user(account)
        return jsonify({'Message': 'New user registered successfully' }), 201
    else:
        return jsonify({"Error": "user already exists"}), 409
            
        
              





@app.route('/api/v2/login', methods=['POST','GET'])
def login_user():
    if request.method =='POST':

        auth = json.loads(request.data)
        
        if not auth or not auth['username'] or not auth['password']:
            return make_response('unauthorized accessss', 401, {'WWW-Authenticate':
                                                                'Basic realm="Login required!"'})
        user = db_obj.query_username(auth['username'])
        if not user:
            return make_response('Could not verify', 401, {'WWW-Authenticate':
                                                        'Basic realm="Login required!"'})
        
        
        if check_password_hash(user["hash_password"], auth['password']):
        
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

    else:
        return jsonify({"Error": "Method Not allowed"})

@app.route('/api/v2/parcels', methods=['POST'])
def create_parcels():
    if request.method =='POST':
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
    else:
        return jsonify({"Error": "Method Not allowed"})

@app.route("/api/v2/parcels", methods=["GET"])
def get_all_parcelss():
    """Implements the get all parcel delivery orders api."""   
    if request.method =='GET':
        parcel_list = db_obj.get_parcels()
        return jsonify({'parcels': parcel_list}), 200
    

@app.route("/api/v2/parcels/<parcel_id>", methods=["GET"])
def get_single_parcel(parcel_id):
    """Implements api to get a specific parcel delivery order.""" 

    parcel = db_obj.get_one_parcel(int(parcel_id))    
    return jsonify({"Parcel": parcel}), 200

@app.route("/api/v2/parcels/<parcel_id>/status", methods=["PUT"])
def update_status(current_user,parcel_id):
    """Implements api that changes parcel delivery order status."""
     
    if not current_user["role"] == "admin":
        return jsonify({"Error":"Unauthorised access"}), 401
    data =json.loads(request.data)
    parcel_status = data["status"]
    if  not parcel_id.isdigit():
        return jsonify({"Error": "Please input correct parcel  id"}), 400     
    elif parcel_status:
        updated = db_obj.update_parcel_status(int(parcel_id), parcel_status)
        return jsonify({"parcel status changed": updated}), 201  
    else:
        return jsonify({"Error": "parcel does not exist"}), 404

@app.route("/api/v2/parcels/<parcel_id>/destination", methods=["PUT"])

def update_destination(parcel_id):
    """Implements api that changes parcel delivery order destination."""
    data =json.loads(request.data)
    parcel_destination = data["destination"]
    if  not parcel_id.isdigit():
        return jsonify({"Error": "Please input correct parcel  id"}), 400     
    elif parcel_destination:
        updated = db_obj.update_parcel_destination(int(parcel_id), parcel_destination)
        return jsonify({"parcel destination changed": updated}), 201  
    else:
        return jsonify({"Error": "parcel does not exist"}), 404


@app.route("/api/v2/parcels/<parcel_id>/presentLocation", methods=["PUT"])
@token_required
def update_presentLocation(current_user,parcel_id):
    """Implements api that changes parcel delivery order presentLocation."""
    if not current_user["role"] == "admin":
        return jsonify({"Error":"Unauthorised access"}), 401
    data =json.loads(request.data)
    parcel_current_location = data["current_location"]
    if  not parcel_id.isdigit():
        return jsonify({"Error": "Please input correct parcel  id"}), 400     
    elif parcel_current_location:
        updated = db_obj.update_parcel_current_location(int(parcel_id), parcel_current_location)
        return jsonify({"parcel presentLocation changed": updated}), 201  
    else:
        return jsonify({"Error": "parcel does not exist"}), 404

def valid_email(email):
    checked_email = db_obj.fetch_user_email(email)

    if checked_email==1:
        return jsonify({'error': 'Sorry user already exists'}), 409
    elif len(email) < 6:
        return jsonify({'error': 'Email can not be less than six\
            characters'}), 400
    elif email.isdigit():
        return jsonify({'error': 'Email format not allowed\
        an email can not only have numbers'}), 400
    elif "@" not in email:
        return jsonify({'error': 'Email format not allowed\
        an email must conatain @'}), 400
    elif "." not in email:
        return jsonify({'error': 'Email format not allowed\
        an email must conatain . character'}), 400
    elif email.startswith("@") or email.startswith("."):
        return jsonify({'error': 'Email format not allowed\
        an email must not start with @ or . character'}), 400
    elif "@." in email:
        return jsonify({'error': 'Email format not allowed an email must not start with @ or . character next to each other'}), 400
    elif ".@" in email:
        return jsonify({'error': 'Email format not allowed an email must not start with @ or . character next to each other'}), 400