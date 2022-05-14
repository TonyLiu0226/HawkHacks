from flask import Flask,request
from db.db_util import *

app = Flask(__name__)

@app.route("/adduser",methods=["POST"])
def adduser():
    pass

@app.route("/validateuser",methods=["POST"])
def validateuser():
    data = request.json()
    email = data.get("email")
    password = data.get("password")

    user_data = get_user(email)
    if user_data:
        if user_data["password"] == password:
            return {"status":"authenticated"},200
        else:
            return {"status":"login failed"},401    

@app.route("/gettech",methods=["GET"])
def gettech():
    with open("./data/languages.txt","r") as file:
        langs = file.read().splitlines()
    
    with open("./data/frameworks.txt","r") as file:
        frameworks = file.read().splitlines()
    
    return {"languages":langs,"frameworks":frameworks}

if __name__ == "__main__":
    app.run(debug=True,port=8080)