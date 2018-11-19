from flask import request, jsonify,make_response,json, Response, abort
from app import create_app
import jwt
from werkzeug.security import check_password_hash
import datetime
from .user_actions import UserActions


user_action_obj =UserActions()



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
        elif 'email' not in data:
            return jsonify({'error': 'Email is requred'}), 400
        elif 'password' not in data:
            return jsonify({'error': 'password is required'}), 400
        email=data["email"]
        password=data['password']          

        if email=="" or password=="":
            return jsonify({"Error": "No user Found"}), 400
            
        else:
            user_action_obj.user_register(username,email, password)
            return jsonify({'Message': 'New user registered successfully' }), 201
    else:
        return jsonify({"Error": "Method Not allowed"})      



@app.route("/api/v1/users", methods=["GET"])
def fetch_all_users():
    if request.method == "GET":
        new_users_lists=user_obj.fetch_all_users()  
        return jsonify({"Users":new_users_lists}), 200

    else:
        return jsonify({"Error": "Method Not allowed"})  

