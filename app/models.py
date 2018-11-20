# from app import app
import psycopg2
from psycopg2.extras import RealDictCursor

class Database:    
    def __init__(self):
        """Connect to the database."""        
        self.conn = psycopg2.connect("dbname=sendit user=postgres password=password host=localhost")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor=self.conn.cursor(cursor_factory=RealDictCursor)

        print("Connected to the database")

    def create_user_table(self):
        """Create table to store users data."""
        user_table = ("CREATE TABLE IF NOT EXISTS users"
                    "(user_id serial  NOT NULL PRIMARY KEY,"                   
                    "username VARCHAR(50) UNIQUE NOT NULL,"
                    "email VARCHAR(80) UNIQUE NOT NULL,"                    
                    "hash_password VARCHAR(200) NOT NULL,"
                    "role VARCHAR(10) NOT NULL)")

        self.cur.execute(user_table)

    def create_parcels_table(self):
        """Create table to store parcel delivery orders."""
        parcels_table = ("CREATE TABLE IF NOT EXISTS Parcels"
                        "(parcel_id serial  NOT NULL PRIMARY KEY,"
                        "destination VARCHAR(50) NOT NULL,"
                        "current_location VARCHAR(50) NOT NULL,"
                        "status VARCHAR(11) NOT NULL,"
                        "user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id))")
        self.cur.execute(parcels_table)

