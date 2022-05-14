import os
from pymongo import MongoClient


DB_CONN_URL = "mongodb+srv://sudo:bp1qvsEZNWvhoPGv@codebook-data.btvbo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

def get_user(email):
    client = MongoClient(DB_CONN_URL)

    try:
        db = client["users"]
        users_data = db["users-data"]
        post = {"_id":email}
        user_data  = users_data.find(post)
        
        if user_data:
            return user_data
        
        else:
            return False
 
    
    except Exception:
        client.close()
        return False