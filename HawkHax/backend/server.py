from flask import Flask,request
from db.db_util import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/adduser",methods=["POST"])
@cross_origin(supports_credentials=True)
def adduser():
    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        reg_user = register_user(data)
        
        if reg_user:
            return {"status":"user added"},200
        else:
            return {"status":"unknown error"},404
    else:
        return {"status","only post endpoints are supported on this endpoint"},404       

@app.route("/validateuser",methods=["POST"])
@cross_origin(supports_credentials=True)
def validateuser():
    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        email = data["email"]
        password = data["password"]

        user_data = get_user(email)
        if user_data:
            if user_data["password"] == password:
                return {"status":"authenticated"},200
            else:
                return {"status":"login failed"},401
        else:
            return {"status":"user does not exist"},401    
    
    else:
        return {"status":"this endpoint only accepts POST requests"},401    

    

@app.route("/gettech",methods=["GET"])
def gettech():
    with open("./data/languages.txt","r") as file:
        langs = file.read().splitlines()
    
    with open("./data/frameworks.txt","r") as file:
        frameworks = file.read().splitlines()
    
    return {"languages":langs,"frameworks":frameworks}

if __name__ == "__main__":
    app.run(debug=True,port=8080)