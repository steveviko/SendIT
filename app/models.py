from app import app
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