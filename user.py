import encryption
from project import Project

class User:
    username = ''
    password = ''
    user_id = ''
    pass_id = ''
    project_list = []


    def __init__(self):
        pass

<<<<<<< HEAD
    def signup(self, usern, passw, db):
=======
    def signup(self, usern, passw):
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        #Check if usern or passw contains ' ' or !, if yes, return error, if not continue and return
        if ' ' in usern or '!' in usern:
            #send error message to frontend
            return
        if ' ' in passw or '!' in passw:
            #send error message to frontend
            return

        #Check if usern already exists in database
        # if usern exists in database:
        # send different error message to frontend
        #
        #

<<<<<<< HEAD
        if db.user_collection.findOne({'username' : usern}).username is None:
            #send error message of username already exists
            return




=======
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391

        # Create usern, passw, userid, passw_id
        User.username = usern
        User.password = passw

        User.user_id = encryption.customEncrypt(usern, 4, 1)
        User.pass_id = encryption.customEncrypt(passw, 4, 1)

        #send user object to database as a new user
<<<<<<< HEAD
        db.user_collection.insertOne(
            {
                'username': User.username,
                'password': User.password,
                'user_id': User.user_id,
                'pass_id': User.pass_id,
                'project_list': User.project_list
            }
        )
=======
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391

        return


<<<<<<< HEAD
    def login(self,usern, passw, db):
=======
    def login(self,usern, passw):
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        #check database for matching usern and passw
        #if match: get object, put data in object attributes, send object to frontend and return
        #if not match: return error message to frontend

<<<<<<< HEAD
        if db.user_collection.findOne({'username': usern}).username is usern and db.user_collection.findOne({'password' : passw}).password is passw:
            User.username = db.user_collection.findOne({'username': usern}).username
            User.password = db.user_collection.findOne({'username': usern}).password
            User.user_id = db.user_collection.findOne({'username': usern}).user_id
            User.pass_id = db.user_collection.findOne({'username': usern}).pass_id
            User.project_list = db.user_collection.findOne({'username': usern}).project_list
            #send to frontend
            return
        else:
            #return error message
            return

    def project_page(self):#implement
        #get all projects of currentUser from database and send to frontend
        pass

    def add_project(self, usern, proj_name, db):
=======
        return

    def project_page(self):
        #get all projects of currentUser from database and send to frontend
        pass

    def add_project(self, usern, proj_name):
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        #create new project object
        curProj = Project()
        #make unique_id for that project
        proj_id = encryption.proj_encrypt()
        curProj.add_proj(usern, proj_id, proj_name)
<<<<<<< HEAD
        curProj.collaborators.append(usern)

        #put curProj in database seperately for project object.
        db.project_collection.insertOne(
            {
                'project_name': curProj.project_name,
                'project_id': curProj.project_id,
                'hw1': 0,
                'hw2': 0,
                'collaborators': curProj.collaborators
            }
        )


        # from username, search user object in database, add project_id to project_list for user
        user_project_list = db.user_collection.findOne({'username': usern}).project_list
        user_project_list.append(proj_id)


        db.user_collection.updateOne({'username':usern}, {"$set": {'project_list': user_project_list}})

=======


        #put curProj in database seperately for project object.
        # from username, search user object in database, add project to project_list for user
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391


        #send to user object to frontend
        return


<<<<<<< HEAD
    def join_project(self, usern, projectid, db):
=======
    def join_project(self, usern, projectid):
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        #check if projectid exist in database
        #if not, return error code to frontend
        #if does, add project to user and add user to project object in both databases

<<<<<<< HEAD
        if db.project_collection.findOne({'project_id': projectid}).project_id is None:
            #return error code
            return
        else:
            collab = db.project_collection.findOne({'project_id': projectid}).collaborators
            collab.append(usern)
            db.project_collection.updateOne({'project_id': projectid}, {"$set": {'collaborators': collab}})


            user_project_list = db.user_collection.findOne({'username': usern}).project_list
            user_project_list.append(projectid)
            db.user_collection.updateOne({'username': usern}, {"$set": {'project_list': user_project_list}})


        #send user object to frontend
        return

    def edit_proj(self, usern, projectid, db):
        #search proj by proj_id in database
        #send project object to frontend (including hw1, hw2, collaborators)

        curProj = Project()

        curProj.project_name = db.project_collection.findOne({'project_id': projectid}).project_name
        curProj.project_id = db.project_collection.findOne({'project_id': projectid}).project_id
        curProj.hw1 = db.project_collection.findOne({'project_id': projectid}).hw1
        curProj.hw2 = db.project_collection.findOne({'project_id': projectid}).hw2
        curProj.collaborators = db.project_collection.findOne({'project_id': projectid}).collaborators


        #send curProj back to frontend
=======
        #send user object to frontend
        return

    def edit_proj(self, usern, projectid):
        #search proj by proj_id in database
        #send project object to frontend (including hw1, hw2, collaborators)
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        return

