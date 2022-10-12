import driver
from database import Database as db
from project import Project
from flask import Flask, request

app = Flask(__name__)

# receive a token
# return the project doc for the project id
@app.route('/project/<project_id>/', methods=['POST'])
# check if there is a token
def get_proj_doc(project_id):
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"
    # below is if token exists
    if request.method == 'POST':
        myquery = {"proj_id": p_id}
        mydoc = db.project_collection.find(myquery)
        for doc in mydoc:
            return doc
    else:
        return "failure"

# receive token, hw1, hw2
# no return
@app.route('/project/<project_id>/checkin', methods=['POST'])
def checkin(project_id):
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"

    # below is if token exists

    if request.method == 'POST':
        # check if this token has permission to access project_id
        cursor = db.user_collection.find({'token': token})  # find the user doc with the token
        for temp in cursor:
            p_id_list = temp['project_list']  # find the user's project list
        if project_id not in p_id_list:  # check if the user has this project
            return "failure"

        # below is if token has permission to this project
        # get hw1 and hw2 from somewhere
        curProject = Project()
        curProject.project_id = project_id

        cursor = db.project_collection.find({'proj_id': project_id})
        for temp in cursor:
            projName = temp['proj_name']
            hard1 = temp['hw1']
            hard2 = temp['hw2']
            collab = temp['collaborators']

        curProject.project_name = projName
        curProject.hw1 = hard1
        curProject.hw2 = hard2
        curProject.collaborators = collab

        Project.checkin_hw(project_id, hw1, hw2)
    else:
        return "failure"

# receive token, hw1, hw2
# no return
@app.route('/project/<project_id>/checkin', methods=['POST'])
def checkout(project_id):
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"

    # below is if token exists
    if request.method == 'POST':
        # check if this token has permission to access project_id
        cursor = db.user_collection.find({'token': token})  # find the user doc with the token
        for temp in cursor:
            p_id_list = temp['project_list']                # find the user's project list
        if project_id not in p_id_list:                     # check if the user has this project
            return "failure"

        # below is if token has permission to this project
        # get hw1 and hw2 from somewhere
        curProject = Project()
        curProject.project_id = project_id

        cursor = db.project_collection.find({'proj_id': project_id})
        for temp in cursor:
            projName = temp['proj_name']
            hard1 = temp['hw1']
            hard2 = temp['hw2']
            collab = temp['collaborators']

        curProject.project_name = projName
        curProject.hw1 = hard1
        curProject.hw2 = hard2
        curProject.collaborators = collab

        Project.checkout_hw(project_id, hw1, hw2)
    else:
        return "failure"

# receive token
# return user doc
@app.route('/user/', methods=['POST'])
def get_user_doc():
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"

    # below is if token exists
    if request.method == 'POST':
        # get the user doc associated with the token
        cursor = db.user_collection.find({'token': token})  # find the user doc with the token
        for userdoc in cursor:
            return userdoc
    else:
        return "failure"

# receive token
# return list of project docs
@app.route('/user/project_documents', methods=['POST'])
def get_user_project_docs():
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"

    if request.method == 'POST':
        cursor = db.user_collection.find({'token': token})  # find the user doc with the token
        for temp in cursor:
            project_id_list = temp['project_list']          # get the array of project ids this user is in

        return db.project_collection.find({"project_id": {"$in": project_id_list}})
    else:
        return "failure"

# receive token and project_name
# create a new project for that user
# no actual return?
# need token and project name from somehwere
@app.route('/user/add_project', methods=['POST'])
def add_new_project():
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"

    if request.method == 'POST':
        # unsure
        currentUser = User()
        currentUser.add_project(username, project_name, db)
        return "success"
    else:
        return "failure"

# receive token, project_id
# add user to project
# no actual return?
@app.route('/user/join_project', methods=['POST'])
def join_project():
    # check token
    if db.user_collection.find({'token': {"$in": token}}).count() != 1:
        return "failure"

    if request.method == 'POST':
        cursor = db.user_collection.find({'token': token})  # find the user doc with the token
        for temp in cursor:
            project_id_list = temp['project_list']          # get the array of project ids this user is in
        project_id_list.append(project_id)                  # add the new project id to the user project list
        db.user_collection.update_one({"token": token},
                                   {"$set": {"project_list": project_id_list}})

        cursor = db.project_collection.find({'project_id': project_id})  # find the project doc with the id
        for temp in cursor:
            collaborator_list = temp['collaborators']  # get the array of usernames in this project
        cursor = db.user_collection.find({'token': token})  # find the user with the doc
        for temp in cursor:
            this_username = temp['username']                # get the token's username
        collaborator_list.append(this_username)             # add the username to the project's username list
        db.project_collection.update_one({"project_id": project_id}, {"$set": {"collaborators": collaborator_list}})

    else:
        return "failure"

# for post, receive username, password
# return pass/fail, user doc
#
# for get, return html, no receive
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        cursor = db.user_collection.find({'username': username})  # find the user doc with the token
        for temp in cursor:
            actual_password = temp['password']
        if password == actual_password:
            return "pass"
        return "fail"
    else:
        return render_template('login.html')

# for post, receive username, password
# return pass/fail
#
# for get, return html, no receive
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        if db.user_collection.find({'username': {"$in": username}}).count() != 0:   # fail if the username already exists
            return "fail"
        # if passwords are unique, leave in below, otherwise take out
        if db.user_collection.find({'password': {"$in": password}}).count() != 0:
            return "fail"
        
        # create new user

        return "signup post"
    else:
        return render_template('signup.html')

# return html, no receive
@app.route('/project_list', methods=['GET'])
def get_project_list_page():
    if request.method == 'GET':
        return render_template('project_list.html')
    else:
        return "failure"

# return html, no receive
@app.route('/project_edit', methods=['GET'])
def get_project_edit_page():
    if request.method == 'GET':
        return render_template('project_list.html')
    else:
        return "failure"

# return html, no receive
@app.route('/project_add', methods=['GET'])
def get_project_add_page():
    if request.method == 'GET':
        return render_template('project_add.html')
    else:
        return "failure"

