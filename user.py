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

    def signup(self, usern, passw):
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


        # Create usern, passw, userid, passw_id
        User.username = usern
        User.password = passw

        User.user_id = encryption.customEncrypt(usern, 4, 1)
        User.pass_id = encryption.customEncrypt(passw, 4, 1)

        #send user object to database as a new user

        return


    def login(self,usern, passw):
        #check database for matching usern and passw
        #if match: get object, put data in object attributes, send object to frontend and return
        #if not match: return error message to frontend

        return

    def project_page(self):
        #get all projects of currentUser from database and send to frontend
        pass

    def add_project(self, usern, proj_name):
        #create new project object
        curProj = Project()
        #make unique_id for that project
        proj_id = encryption.proj_encrypt()
        curProj.add_proj(usern, proj_id, proj_name)


        #put curProj in database seperately for project object.
        # from username, search user object in database, add project to project_list for user


        #send to user object to frontend
        return


    def join_project(self, usern, projectid):
        #check if projectid exist in database
        #if not, return error code to frontend
        #if does, add project to user and add user to project object in both databases

        #send user object to frontend
        return

    def edit_proj(self, usern, projectid):
        #search proj by proj_id in database
        #send project object to frontend (including hw1, hw2, collaborators)
        return

