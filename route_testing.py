import driver
from database import Database as db
from project import Project
from flask import Flask, request, jsonify, render_template
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import methods
import copy

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

hardware_doc_test = {
    "maxHW1": 0,
    "maxHW2": 0,
    "availHW1": 0,
    "availHW2": 0
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

def clear3():
    hardware_doc_test["maxHW1"] = 0
    hardware_doc_test["maxHW2"] = 0
    hardware_doc_test["availHW1"] = 0
    hardware_doc_test["availHW2"] = 0


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # need to check if username and password match

        # debugging method
        clear()
        clear2()
        clear3()

        uname = request.json.get('username')
        pword = request.json.get('password')

        cursor = db.user_collection.find({'username': uname})
        for temp in cursor:
            someuserdocument["username"] = temp['username']
            someuserdocument["password"] = temp['password']
            someuserdocument["user_id"] = temp['user_id']
            someuserdocument["password_id"] = temp['password_id']
            someuserdocument["token"] = temp['token']
            someuserdocument["project_list"] = temp['project_list']
        if someuserdocument['username'] == '':
            return "user " + str(someuserdocument['username']) + " does not exist"
        if someuserdocument['password'] != pword:
            return "incorrect password for user " + str(someuserdocument['username'])

        return {
            "pass/fail": "pass",
            "status": "successful login with username " + uname + " and password " + pword,
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
        clear2()
        clear3()

        uname = request.json.get('username')
        pword = request.json.get('password')

        cursor = db.user_collection.find({'username': uname})
        for temp in cursor:
            someuserdocument["username"] = temp['username']
            someuserdocument["password"] = temp['password']
            someuserdocument["user_id"] = temp['user_id']
            someuserdocument["password_id"] = temp['password_id']
            someuserdocument["token"] = temp['token']
            someuserdocument["project_list"] = temp['project_list']

        if someuserdocument['username'] != '':
            return {
                "pass/fail": "fail",
                "report": "username " + uname + " already exists"
            }

        newuser = {
            "username": uname,
            "password": pword,
            "user_id": "",
            "password_id": "",
            "token": "",
            "project_list": []
        }

        x = db.user_collection.insert_one(newuser)

        return {
            "pass/fail": "pass",
            "status": "successful signup with username " + uname + " and password " + pword,
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
        clear()
        clear2()
        clear3()

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
        clear3()

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
        # debug
        #else:
            #return {
                #"status": "pass",
                #"token used": my_token,
                #"project doc": proj_doc_test
            #}

        # create methods.py for now to do checkin and checkout

        #methods.hardware_checkin(hw1, hw2)
        methods.project_checkin(project_id, hw1, hw2)

        cursor = db.hardware_collection.find({'maxHW1': {"$exists": "true"}})
        for temp in cursor:
            hardware_doc_test['maxHW1'] = temp['maxHW1']
            hardware_doc_test['maxHW2'] = temp['maxHW2']
            hardware_doc_test['availHW1'] = temp['availHW1']
            hardware_doc_test['availHW2'] = temp['availHW2']

        cursor = db.project_collection.find({'project_id': project_id})
        for temp in cursor:
            proj_doc_test["project_name"] = temp['project_name']
            proj_doc_test["project_id"] = temp['project_id']
            proj_doc_test["hw1"] = temp['hw1']
            proj_doc_test["hw2"] = temp['hw2']
            proj_doc_test["collaborators"] = temp['collaborators']

        if methods.status_list:
            if -3 in methods.status_list:
                if -4 in methods.status_list:
                    return "not enough HW1 and HW2"
                return "not enough HW1"
            if -4 in methods.status_list:
                return "not enough HW2"

        return {
            "hardware doc": hardware_doc_test,
            "project doc": proj_doc_test,
            "status list": methods.status_list
        }


    else:
        return "fail"

@app.route('/project/<int:project_id>/checkout', methods= ['POST'])
def checkout(project_id):
    if request.method == 'POST':
        # debugging method
        clear()
        clear2()
        clear3()

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
        # debug
        #else:
            #return {
                #"status": "pass",
                #"token used": my_token,
                #"project doc": proj_doc_test
            #}

        methods.project_checkout(project_id, hw1, hw2)

        cursor = db.hardware_collection.find({'maxHW1': {"$exists": "true"}})
        for temp in cursor:
            hardware_doc_test['maxHW1'] = temp['maxHW1']
            hardware_doc_test['maxHW2'] = temp['maxHW2']
            hardware_doc_test['availHW1'] = temp['availHW1']
            hardware_doc_test['availHW2'] = temp['availHW2']

        cursor = db.project_collection.find({'project_id': project_id})
        for temp in cursor:
            proj_doc_test["project_name"] = temp['project_name']
            proj_doc_test["project_id"] = temp['project_id']
            proj_doc_test["hw1"] = temp['hw1']
            proj_doc_test["hw2"] = temp['hw2']
            proj_doc_test["collaborators"] = temp['collaborators']

        if methods.status_list:
            if -1 in methods.status_list:
                if -2 in methods.status_list:
                    return "not enough available HW1 and HW2"
                return "not enough available HW1"
            if -2 in methods.status_list:
                return "not enough available HW2"

        return {
            "hardware doc": hardware_doc_test,
            "project doc": proj_doc_test
        }

    else:
        return "fail"

@app.route('/user/', methods= ['POST'])
def get_user():
    # receive a token from frontend, return user doc
    if request.method == 'POST':
        clear()
        clear2()
        clear3()

        my_token = request.json.get('token')

        cursor = db.user_collection.find({'token': my_token})
        for temp in cursor:
            someuserdocument["username"] = temp['username']
            someuserdocument["password"] = temp['password']
            someuserdocument["user_id"] = temp['user_id']
            someuserdocument["password_id"] = temp['password_id']
            someuserdocument["token"] = temp['token']
            someuserdocument["project_list"] = temp['project_list']

        if someuserdocument['token'] == '':
            return {
                "status": "fail",
                "report": "token " + str(my_token) + " does not exist"
            }

        return {
            "user doc": someuserdocument
        }

    else:
        return "fail"

@app.route('/user/project_documents', methods= ['POST'])
# receive token from frontend
def get_user_projects():
    if request.method == 'POST':
        clear()
        clear2()
        clear3()

        my_token = request.json.get('token')

        cursor = db.user_collection.find({'token': my_token})
        for temp in cursor:
            someuserdocument["username"] = temp['username']
            someuserdocument["password"] = temp['password']
            someuserdocument["user_id"] = temp['user_id']
            someuserdocument["password_id"] = temp['password_id']
            someuserdocument["token"] = temp['token']
            someuserdocument["project_list"] = temp['project_list']

        if someuserdocument['token'] == '':
            return {
                "status": "fail",
                "report": "token " + str(my_token) + " does not exist"
            }

        project_id_list = someuserdocument['project_list']

        # debug
        #return {
            #"project list": project_id_list
        #}

        project_doc_list = []
        for project_id in project_id_list:
            clear2()

            cursor = db.project_collection.find({'project_id': project_id})
            for temp in cursor:
                proj_doc_test["project_name"] = temp['project_name']
                proj_doc_test["project_id"] = temp['project_id']
                proj_doc_test["hw1"] = temp['hw1']
                proj_doc_test["hw2"] = temp['hw2']
                proj_doc_test["collaborators"] = temp['collaborators']

            # uncomment this is it is possible to have projects listed that do not exist
            #if proj_doc_test['project_id'] == '':
                #continue

            tempdoc = copy.deepcopy(proj_doc_test)
            project_doc_list.append(tempdoc)

        #for item in project_doc_list:
            #print(item)
        #print(project_doc_list)

        return project_doc_list

    else:
        return "fail"

@app.route('/user/add_project', methods= ['POST'])
# receive token and project name from frontend
def create_project():
    if request.method == 'POST':
        clear()
        clear2()
        clear3()

        my_token = request.json.get('token')
        pname = request.json.get('project_name')

        cursor = db.user_collection.find({'token': my_token})
        for temp in cursor:
            someuserdocument["username"] = temp['username']
            someuserdocument["password"] = temp['password']
            someuserdocument["user_id"] = temp['user_id']
            someuserdocument["password_id"] = temp['password_id']
            someuserdocument["token"] = temp['token']
            someuserdocument["project_list"] = temp['project_list']

        if someuserdocument['token'] == '':
            return {
                "status": "fail",
                "report": "token " + str(my_token) + " does not exist"
            }

        project_id = 0

        cursor = db.project_collection.find({'project_id': project_id})
        ids = db.project_collection.distinct('project_id')

        # debug
        #for id in ids:
            #print(id)
        #return ids

        while project_id in ids:
            project_id = project_id + 1

        # debug
        #return "create id of " + str(project_id)

        new_project = {
            "project_name": pname,
            "project_id": project_id,
            "hw1": "",
            "hw2": "",
            "collaborators": []
        }
        new_project['collaborators'].append(someuserdocument['username'])
        someuserdocument['project_list'].append(project_id)
        plist = someuserdocument['project_list']

        x = db.project_collection.insert_one(new_project)
        db.user_collection.update_one({"token": my_token}, {"$set": {"project_list": plist}})

        return "success"

    else:
        return "fail"


app.run(debug = True, host='0.0.0.0', port=8080)
