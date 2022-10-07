from user import User
from project import Project
<<<<<<< HEAD
from database import Database
=======
import database
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
from hardware import Hardware





def take_request(global_request):
    #do forever while loop until new request comes in
    #get request data
    #check if its the same user
    #look for requestType

    requestType = ''

    return requestType




if __name__ == '__main__':

<<<<<<< HEAD
    #initialize database
    db = Database()

    #Take request
    global_request = ''

    #Through hardware database initialize global
    maxHW1 = db.hardware_collection.find_one().maxHW1
    maxHW2 = db.hardware_collection.find_one().maxHW2

    availHW1 = db.hardware_collection.find_one().availHW1
    availHW2 = db.hardware_collection.find_one().availHW2

    # maxHW1 = 1000
    # maxHW2 = 1000
    #                   initialization when database has not been set.
    # availHW1 = 1000
    # availHW2 = 1000
=======
    #Take request
    global_request = ''

    #Through hardware database initialize global hardware
    maxHW1 = 1000
    maxHW2 = 1000

    availHW1 = 1000
    availHW2 = 1000
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
    globalHardware = Hardware(maxHW1, maxHW2, availHW1, availHW2)

    while True:
        requestType = take_request(global_request)

        if requestType == 'signup':
            #get username and password from request
            username = ''
            password = ''

            currentUser = User()
<<<<<<< HEAD
            errcheck = currentUser.signup(username, password, db)
=======
            errcheck = currentUser.signup(username, password)
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391


        elif requestType == 'login':
            #get username and password from request
            username = ''
            password = ''


            currentUser = User()
<<<<<<< HEAD
            currentUser.login(username, password, db)
=======
            currentUser.login(username, password)
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391


        elif requestType == 'logout':
            #Assumely do nothing since frontend does everything here
            pass


<<<<<<< HEAD
        elif requestType == 'project_page': #to implement
            #get username from request
            #from username go to database and find user object
            #could send entire user
=======
        elif requestType == 'project_page':
            #get username from request
            #from username go to database and find user object
            #could send entire user object or just object_list[]
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
            pass


        elif requestType == 'add_project':
            # find username, project_name in request
            username = ''
            project_name = ''

            currentUser = User()
<<<<<<< HEAD
            currentUser.add_project(username, project_name, db)
=======
            currentUser.add_project(username, project_name)
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391

        elif requestType == 'join_project':
            # find username, unique project_id in request
            username = ''
            project_id = ''

            currentUser = User()
<<<<<<< HEAD
            currentUser.join_project(username, project_id, db)
=======
            currentUser.join_project(username, project_id)
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391

        elif requestType == 'edit_proj':
            # find unique username, unique project_id in request
            username = ''
            project_id = ''

            currentUser = User()
<<<<<<< HEAD
            currentUser.edit_proj(username, project_id, db)

        elif requestType == 'check_out_hw': #implement pls
=======
            currentUser.edit_proj(username, project_id)

        elif requestType == 'check_out_hw':
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
            #find unique project_id, hw1, hw2 in request
            project_id = ''
            hw1 = 0
            hw2 = 0

            curProject = Project()
<<<<<<< HEAD
            #find curProject attributes and put in curProject from database
            curProject.project_name = db.project_collection.find({'proj_id': project_id}).projname
            curProject.project_id = project_id
            curProject.hw1 = db.project_collection.find({'proj_id': project_id}).hw1
            curProject.hw2 = db.project_collection.find({'proj_id': project_id}).hw2
            curProject.collaborators = db.project_collection.find({'proj_id': project_id}).collab
=======
            #find curProject attributes and put in curProject
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391


            Project.checkout_hw(project_id,hw1,hw2)

<<<<<<< HEAD
        elif requestType == 'check_in_hw': #implement pls
=======
        elif requestType == 'check_in_hw':
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
            # find unique project_id, hw1, hw2 in request
            project_id = ''
            hw1 = 0
            hw2 = 0

            curProject = Project()
<<<<<<< HEAD
            # find curProject attributes and put in curProject from database
            curProject.project_name = db.project_collection.find({'proj_id': project_id}).projname
            curProject.project_id = project_id
            curProject.hw1 = db.project_collection.find({'proj_id': project_id}).hw1
            curProject.hw2 = db.project_collection.find({'proj_id': project_id}).hw2
            curProject.collaborators = db.project_collection.find({'proj_id': project_id}).collab
=======
            # find curProject attributes and put in curProject
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391

            Project.checkin_hw(project_id, hw1, hw2)
