import os
from werkzeug.security import generate_password_hash, check_password_hash
from app import create_app
from app.models import Database

db = Database()
cursor =db.cur
dictcur=db.dict_cursor



class DbOperations:
    def __init__(self):
        self.connect=Database()
    
    def add_user(self,account):
        """ insert a new user into the users table """
        command = "INSERT INTO users(username, email,hash_password, role) VALUES(\
                '{}',  '{}', '{}', 'user')".format(account["username"],  account["email"]\
                , generate_password_hash(account["hash_password"]))
        cursor.execute(command)
        return account

    def check_username(self, account_username):
        command = "SELECT user_id,username,hash_password,role from users WHERE username= '{}'".format(account_username['username'])
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

    def query_username(self, account_username):
        command = "SELECT user_id,username,hash_password,role from users WHERE username= '{}'".format(account_username)
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

    def add_parcel(self, parcel,user_id):
        """Adds parcel to the parcel list."""
        for k, v in parcel.items():
            parcel[k] = (v)
        command="INSERT INTO parcels(item, description, status, user_id,current_location, destination) VALUES(\
        %s, %s, %s, %s, %s, %s)"
        cursor.execute(command,(parcel["item"],parcel["description"], "pending", user_id,parcel["current_location"], parcel["destination"]))
        return parcel

    def get_parcels(self):
        """Returns all parcel delivery orders in the parcel list."""
        command="SELECT parcel_id, item,description,status,user_id, current_location, destination FROM parcels"
    #    INNER JOIN users ON parcels.user_id = users.user_id
        dictcur.execute(command) 
        data=dictcur.fetchall()     
        return data  

    def get_one_parcel(self, parcel_id):
        """Returns a specific delivery order from the parcel list."""
        command = "SELECT * FROM parcels WHERE parcel_id ='{}'".format(parcel_id)
        dictcur.execute(command)
        one_parcel= dictcur.fetchone()
        return one_parcel

    def update_parcel_status(self, parcel_id, status):
        """Updates the status of a parcel."""
        command = "UPDATE parcels SET status='{}' WHERE parcel_id ='{}'".format(status,parcel_id)
        cursor.execute(command)
        return_parcel_status = "SELECT * FROM parcels WHERE parcel_id = '{}'".format(parcel_id)
        dictcur.execute(return_parcel_status)
        data = dictcur.fetchall()
        return data

    def update_parcel_destination(self, parcel_id, destination):
        """Updates the destination  of a parcel."""
        command = "UPDATE parcels SET destination='{}' WHERE parcel_id ='{}'".format(destination,parcel_id)
        cursor.execute(command)
        return_parcel_destination = "SELECT * FROM parcels WHERE parcel_id = '{}'".format(parcel_id)
        dictcur.execute(return_parcel_destination)
        data = dictcur.fetchall()
        return data

    def update_parcel_current_location(self, parcel_id, current_location):
        """Updates the current_location  of a parcel."""
        command = "UPDATE parcels SET current_location='{}' WHERE parcel_id ='{}'".format(current_location,parcel_id)
        cursor.execute(command)
        return_parcel_current_location = "SELECT * FROM parcels WHERE parcel_id = '{}'".format(parcel_id)
        dictcur.execute(return_parcel_current_location)
        data = dictcur.fetchall()
        return data
    # def hash_password(self,hashed_password, login_password):
    #     return check_password_hash(hashed_password["hash_password"], login_password["hash_password"])

    # def fetch_user(self, username):
    #     query = self.query_user(username)
    #     return query.fetchone()

    def query_user(self, account):
        command = "SELECT * FROM users WHERE username= '{}'".format(account["username"])
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

        