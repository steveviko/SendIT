from flask import request, jsonify,make_response, redirect, json, Response, abort
from app import create_app
import jwt
from werkzeug.security import check_password_hash
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





