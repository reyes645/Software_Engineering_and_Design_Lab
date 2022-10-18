import driver
from database import Database as db
from project import Project
from flask import Flask, request, jsonify, render_template
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

someuserdocument = {
    "username": "",
    "password": "",
    "user_id": "",
    "password_id": "",
    "token": "",
    "project_list": []

}

def clear():
    someuserdocument["username"] = ""
    someuserdocument["password"] = ""
    someuserdocument["user_id"] = ""
    someuserdocument["password_id"] = ""
    someuserdocument["token"] = ""
    someuserdocument["project_list"] = []


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # need to check if username and password match

        # debugging method
        clear()

        uname = request.json.get('username')
        pword = request.json.get('password')

        someuserdocument["username"] = uname
        someuserdocument["password"] = pword

        return {
            "pass/fail": "pass",
            "status": "trying to login with username " + uname + " and password " + pword,
            "user_document": someuserdocument
        }
    else:
        return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # need to check if username is unique

        # debugging method
        clear()

        uname = request.json.get('username')
        pword = request.json.get('password')

        someuserdocument["username"] = uname
        someuserdocument["password"] = pword

        return {
            "pass/fail": "pass",
            "status": "trying to signup with username " + uname + " and password " + pword,
        }
    else:
        return render_template("signup.html")

@app.route('/project_list', methods = ['GET'])
def project_list():
    if request.method == 'GET':
        return render_template("project_list.html")
    else:
        return "fail"

@app.route('/project_edit', methods = ['GET'])
def project_edit():
    if request.method == 'GET':
        return render_template("project_edit.html")
    else:
        return "fail"

@app.route('/project_add', methods = ['GET'])
def project_add():
    if request.method == 'GET':
        return render_template("project_add.html")
    else:
        return "fail"


app.run(debug = True, host='0.0.0.0', port=8080)
