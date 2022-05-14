import os
from pymongo import MongoClient


DB_CONN_URL = "mongodb+srv://sudo:bp1qvsEZNWvhoPGv@codebook-data.btvbo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

def get_user(email):
    client = MongoClient(DB_CONN_URL)

    try:
        db = client["users"]
        users_data = db["users-data"]
        post = {"_id":email}
        user_data  = users_data.find_one(post)
        
        if user_data:
            return user_data
        
        else:
            return False
 
    
    except Exception as e:
        client.close()
        return False
    
def register_user(details):
    client = MongoClient(DB_CONN_URL)
    try:
        db = client["users"]
        users_data = db["users-data"]
        users_data.insert_one(details)
        return True
    except Exception as e:
        print(e)
        client.close()
        return False