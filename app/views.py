from flask import request, jsonify,make_response, redirect, json, Response, request, abort
from app import create_app
import jwt
from werkzeug.security import check_password_hash
import datetime
from user import User


user_obj =User()



app = create_app()
app.config['SECRET_KEY'] = 'usersecret'

        
@app.route('/api/v12/auth/signup', methods=['POST'])
def signup_user():
    if request.method == 'POST':
        #data from the user  
        result = request.data
        data=json.loads(result)
        if not data:
            return jsonify({'error': 'unsupported Request'}), 400
        elif 'email' not in data:
            return jsonify({'error': 'Email is requred'}), 400
        elif 'password' not in data:
            return jsonify({'error': 'password is required'}), 400
        email=data["email"]
        password=data['password']          

        if email=="" or password=="":
            return jsonify({"Error": "No user Found"}), 400
            
        else:
            user_obj.register_user(email, password)
            return jsonify({'Message': 'New user registered successfully' }), 201
    else:
        return jsonify({"Error": "Method Not allowed"})      





