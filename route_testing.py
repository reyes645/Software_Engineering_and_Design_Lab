import driver
from database import Database as db
from project import Project
from flask import Flask, request, jsonify, render_template
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import methods

app = Flask(__name__)

someuserdocument = {
    "username": "",
    "password": "",
    "user_id": "",
    "password_id": "",
    "token": "",
    "project_list": []

}

proj_doc_test = {
    "project_name": "",
    "project_id": "",
    "hw1": "",
    "hw2": "",
    "collaborators": []
}

def clear():
    someuserdocument["username"] = ""
    someuserdocument["password"] = ""
    someuserdocument["user_id"] = ""
    someuserdocument["password_id"] = ""
    someuserdocument["token"] = ""
    someuserdocument["project_list"] = []

def clear2():
    proj_doc_test["project_name"] = ""
    proj_doc_test["project_id"] = ""
    proj_doc_test["hw1"] = ""
    proj_doc_test["hw2"] = ""
    proj_doc_test["collaborators"] = []


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

@app.route('/project/<int:project_id>', methods = ['POST'])
# data from frontend: token, project_id in url
def get_proj_doc(project_id):
    if request.method == 'POST':
        # debugging method
        clear2()

        my_token = request.json.get('token')
        #cursor = db.user_collection.find({'token': my_token})
        #for temp in cursor:
            #proj_list = temp['project_list']
        #if project_id not in proj_list:
            #return {
                #"status": "fail",
                #"token": my_token,
                #"report": "this user does not have access to project " + str(project_id)
            #}

        cursor = db.project_collection.find({'project_id': project_id})
        for temp in cursor:
            proj_doc_test["project_name"] = temp['project_name']
            proj_doc_test["project_id"] = temp['project_id']
            proj_doc_test["hw1"] = temp['hw1']
            proj_doc_test["hw2"] = temp['hw2']
            proj_doc_test["collaborators"] = temp['collaborators']
        if proj_doc_test['project_id'] == "":
            return {
                "status": "fail",
                "token used": my_token,
                "explanation": "project id " + str(project_id) + " does not exist"
            }
        return {
            "token used": my_token,
            "project doc": proj_doc_test
        }
    else:
        return "fail"

@app.route('/project/<int:project_id>/checkin', methods= ['POST'])
# data from frontend: token, hw1, hw2, project id in url
# checkin means you are returning data
def checkin(project_id):
    if request.method == 'POST':
        # debugging method
        clear()
        clear2()

        hw1 = request.json.get('hw1')
        hw2 = request.json.get('hw2')

        my_token = request.json.get('token')

        # debug
        # successfully gets token, hw1, hw2 when from json
        #return {
            #"token": my_token,
            #"hw1": hw1,
            #"hw2": hw2,
            #"project id": project_id
        #}

        cursor = db.user_collection.find({'token': my_token})

        # successfully retrieves information using token
        for temp in cursor:
            someuserdocument["username"] = temp['username']
            someuserdocument["password"] = temp['password']
            someuserdocument["user_id"] = temp['user_id']
            someuserdocument["password_id"] = temp['password_id']
            someuserdocument["token"] = temp['token']
            someuserdocument["project_list"] = temp['project_list']

        # checking if token exists
        if someuserdocument['token'] == '':
            return {
                "status": "fail",
                "report": "token " + str(my_token) + " does not exist"
            }
        # debug
        #else:
            #return {
                #"status": "pass",
                #"report": "token " + str(my_token) + " was found",
                #"user_doc": someuserdocument
            #}


        # checking project list
        # check this user's projects
        proj_list = someuserdocument['project_list']
        if project_id not in proj_list:
            return {
                "status": "fail",
                "token used": my_token,
                "report": "this user does not have access to project " + str(project_id)
            }
        # debug
        #else:
            #return {
                #"token": my_token,
                #"status": "pass",
                #"report": "user with token " + str(my_token) + " has access to project " + str(project_id)
            #}

        cursor = db.project_collection.find({'project_id': project_id})
        for temp in cursor:
            proj_doc_test["project_name"] = temp['project_name']
            proj_doc_test["project_id"] = temp['project_id']
            proj_doc_test["hw1"] = temp['hw1']
            proj_doc_test["hw2"] = temp['hw2']
            proj_doc_test["collaborators"] = temp['collaborators']
        if proj_doc_test['project_id'] == "":
            return {
                "status": "fail",
                "token used": my_token,
                "explanation": "project id " + str(project_id) + " does not exist"
            }
        else:
            return {
                "status": "pass",
                "token used": my_token,
                "project doc": proj_doc_test
            }

        # create methods.py for now to do checkin and checkout
        #methods.project_checkin(project_id, hw1, hw2)


    else:
        return "fail"


app.run(debug = True, host='0.0.0.0', port=8080)
